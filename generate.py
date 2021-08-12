import json
import os
import pprint  # pylint: disable=unused-import  # for testing
import re
import shutil
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Type, Union

import requests
import statham.schema.parser
import statham.serializers.python
from jinja2 import Template
from json_ref_dict import RefDict, materialize
from statham.schema.elements import Object
from statham.titles import title_labeller

API_SCHEMA = "https://api2.toshl.com/schema/"
SCHEMAS = [
    "user",
    "notification",
    "notification.list",
    # summary (no profile="..." listed at GET /me/summary)
    # setting (/me/settings returns profile="https://api2.toshl.com/schema/user")
    # device (/me/devices returns profile="https://api2.toshl.com/schema/user")
    # app (/me/apps returns profile="https://api2.toshl.com/schema/user")
    # payment (/me/payments returns profile="https://api2.toshl.com/schema/payment.list", but that doesn't exist. There seems to be a "Payment" model in the user schema, though?)
    # promos (/me/promos/foo returns profile="https://api2.toshl.com/schema/promos", but that doesn't exist)
    # shares (/me/shares returns profile="https://api2.toshl.com/schema/shares", but that doesn't exist)
    # steps (/me/steps returns profile="https://api2.toshl.com/schema/step.list", but that doesn't exist)
    # reports (no profile="..." listed at GET /reports)
    "account",
    "account.list",
    "repeat",
    # institutions (/institutions returns profile="https://api2.toshl.com/schema/institution.list", but that doesn't exist)
    # countries (/bank/countries returns profile="https://api2.toshl.com/schema/institution.country.list", but that doesn't exist)
    # connections (/bank/connections returns profile="https://api2.toshl.com/schema/connection.list", but that doesn't exist)
    # imports (/bank/imports returns profile="https://api2.toshl.com/schema/import.list", but that doesn't exist)
    # planning (/planning returns profile="https://api2.toshl.com/schema/planning", but that doesn't exist)
    "entry",
    "entry.list",
    "entry.sum",
    "entry.sum.list",
    "location",
    "location.list",
    #"review",
    #"review.list"
    #"entries.timeline",
    #"entries.timeline.list",
    "budget",
    "budget.list",
    "category",
    "category.list",
    "category.sum",
    "category.sum.list",
    "tag",
    "tag.list",
    "tag.sum",
    "tag.sum.list",
    "currency",
    "export",
    "export.list",
    # "export.filters",
    "image"
]

ObjectDict = Dict[str, Any]
PythonSchema = Dict[str, Any]

def fix(obj: ObjectDict) -> ObjectDict:
    # Upgrade number/integer property ranges to JSON Schema draft 07 spec
    # (statham doesn't like the old booleans)
    type_ = obj.get("type", None)

    def set_del_exclusive(excl_minmax:str, minmax:str):
        if excl_minmax in obj:
            if obj[excl_minmax]:
                obj[excl_minmax] = obj[minmax]
                del obj[minmax]
            else:
                del obj[excl_minmax]

    if type_ in ("number", "integer"):
        set_del_exclusive("exclusiveMinimum", "minimum")
        set_del_exclusive("exclusiveMaximum", "maximum")

    # Replace type of 'date' (which is invalid)
    if type_ == "date":
        obj.update({"type": "string", "format":"date"})

    # Retitle objects to their original Java names, because the others are not unique
    if type_ == "object" and "javaType" in obj:
        obj["title"] = obj['javaType'].split('.')[-1]
    
    return obj

def download_schema(download_dir:Path):
    """Download JSON schema from Toshl API"""
    download_dir.mkdir(parents=True, exist_ok=True)

    # Get schemas
    for schema_path in SCHEMAS:
        response = requests.get(API_SCHEMA + schema_path)
        if response.ok:
            json_path = download_dir.joinpath(schema_path + '.json')
            json_path.write_text(response.text)

def fix_schema(original_dir:Path, dest_dir:Path):
    """Fix schema in a given directory and store in another one"""
    dest_dir.mkdir(parents=True, exist_ok=True)
    # Create a dummy item.json for the fixed schemas
    dummies = [
        "item.json",
        "export.filters.json",
        "export.format.json",
        "export.resource.json"
    ]
    for dummy_json in dummies:
        item = {
            "type": "object",
            "properties": {},
            "description": f"Dummy Item, because Toshl dev do not include {dummy_json}"
        }
        dummy_data = json.dumps(item, sort_keys=True, indent=4)
        dest_dir.joinpath(dummy_json).write_text(dummy_data)

    # Fix all of the schemas, and while we're at it,
    # create a top level object with definitions for all schemas.
    top: Dict[str, Dict[str, Dict[str, Any]]] = {"definitions": {}}
    for original_schema_file_path in original_dir.glob('*.json'):
        top["definitions"][original_schema_file_path.stem] = {"$ref": f"{original_schema_file_path.name}#"}

        fixed = None
        with original_schema_file_path.open() as f:
            fixed = json.load(f, object_hook=fix)

        with dest_dir.joinpath(original_schema_file_path.name).open('w') as f:
            json.dump(fixed, f, sort_keys=True, indent=4)

    with dest_dir.joinpath('top.json').open('w') as f:
        json.dump(top, f, sort_keys=True, indent=4)


def get_python_schema(schema_dir:Path) -> PythonSchema:
    """Convert the JSON schemas into Python objects using statham"""
    # As the JSON schemas use references to other files,
    # it is better to enter to their directory
    curr_dir = Path.cwd()
    os.chdir(schema_dir)
    schema = materialize(RefDict('top.json'), context_labeller=title_labeller())
    os.chdir(curr_dir)

    return schema

Crumb = Tuple[str, ...]
Method = str
Href = str
Argument = Optional[Type[Object]]
ReturnType = Optional[Type[Object]]
ListAPIMethods = List[Tuple[Crumb, Method, Href, Argument, ReturnType]]
APIMethod = Dict[str, Union[Method, Href, Argument, ReturnType]]
DictAPIMethods = Dict[Crumb, APIMethod]


def get_api_methods(schema:PythonSchema) -> ListAPIMethods:
    """Retrieve the API Methods from the schema and by using Returned Types"""
    # Import our new return types.
    import toshling.models.return_types

    api_methods: ListAPIMethods = []
    for n, s in schema['definitions'].items():
        # Get links
        # (handle the extra crap statham puts into the definitions object)
        links = []
        try:
            links = s.get("links", [])
        except Exception:
            pass

        for link in links:
            href = link["href"]

            method = link.get("method", "GET")

            crumbs = [
                crumb.split('?')[0]
                for crumb in href.split('/')
                if crumb and crumb[0] != "{"
            ]
            crumbs.append(link["rel"])
            if crumbs[-1] == "self":
                crumbs[-1] = "get"
            if crumbs[-1] == crumbs[-2]:
                crumbs = crumbs[:-1]
            
            # Get the argument type.
            argument = None
            if "schema" in link:
                # Sub in a sensible title and parse the argument structure.
                link["schema"]["title"] = '.'.join(crumbs + ["argument"])
                argument = statham.schema.parser.parse_element(link['schema'])

                # Toshl uses `!attribute` a bunch, which statham turns into
                # `exclamation_mark_attribute`. Change these to `not_attribute`
                negated_keys = [
                    key for key in argument.properties if key[:16] == "exclamation_mark"
                ]
                for negated_key in negated_keys:
                    not_key = "not" + negated_key[16:]
                    argument.properties[not_key] = argument.properties.pop(negated_key)

            # Try guess some return types.
            return_ = None
            if crumbs[-1] in {'get', 'list', 'update'}:
                guesses = []
                
                guesses.append(s['title'])

                class_parts = [p.capitalize() for p in n.split('.')]
                if class_parts[-1] in {'List'}:
                    class_parts = class_parts[:-1]
                guesses.append(''.join(class_parts))

                for guess in guesses:
                    try:
                        return_ = getattr(toshling.models.return_types, guess)
                        break
                    except Exception as e:
                        pass

            api_methods.append((tuple(crumbs), method, href, argument, return_))

    return api_methods


def filter_api_methods(api_methods: ListAPIMethods) -> DictAPIMethods:
    """Filter API Methods to discard, modify or add as needed"""
    # Toshl has a lot of duplicate method/endpoint pairs, lots of which are invalid.
    # We will take only those with the longest crumbs
    # (which usually means there is a verb on the end).
    # Also discard/modify/add methods we know need modifying.
    discard: Set[Crumb] = {
        ('accounts', 'account'),
        ('budgets', 'budget'),
        ('categories', 'category'),
        ('entries', 'entry'),
        ('entries', 'locations', 'location'),
        ('entries', 'transactions'),
        ('entries', 'transactions', 'repeats', 'repeating transactions'),
        ('entries', 'transaction_pair'),
        ('months', 'month')
    }
    modify: DictAPIMethods = {}
    add: DictAPIMethods = {}

    seen: Set[Tuple[str, str]] = set()
    filtered_api_methods: DictAPIMethods = {}
    sorted_apis = sorted(api_methods, key=lambda x: (x[2].split('?')[0], x[1], -len(x[0])))
    for crumbs, method, href, arg, ret in sorted_apis:
        key = (href.split('?')[0], method)
        if key not in seen and crumbs not in discard:
            api_method = {'method': method, 'href': href, 'argument': arg, 'return': ret}
            api_method.update(modify.get(crumbs, {}))
            filtered_api_methods[crumbs] = api_method
        seen.add(key)
    filtered_api_methods.update(add)
    return filtered_api_methods


# Automatically generate Python code for the endpoints.
ListMethods = List[Dict[str, Any]]
SubClasses = Set[Tuple[str, str]]
Class = Dict[str, Union[str, ListMethods, SubClasses]]
Classes = Dict[str, Class]

def get_classes(filtered_api_methods) -> Classes:
    """Return a list of all Classes to create for EndPoints"""
    classes: Classes = defaultdict(lambda: {"name": "", "methods": [], "subclasses":set()})
    for crumbs, api_method in filtered_api_methods.items():
        classname = ''.join(n.capitalize() for n in crumbs[:-1])
        class_ = classes[classname]
        class_["name"] = classname

        method = {'name': crumbs[-1]}
        method.update(api_method)
        class_["methods"].append(method)  # type:ignore # different types

        if len(crumbs) > 2:
            top_class = classes[''.join(n.capitalize() for n in crumbs[:-2])]
            subclass = (crumbs[-2], classname)
            top_class["subclasses"].add(subclass)  # type:ignore # different types

    return classes


def main(update_json: bool = True):
    # After downloading the schema from Toshl API we will have to do some cleaning
    # (some types need to be modified, some json are missing, etc.)
    original_schema_path = Path('schemas/original/')
    fixed_schema_path = Path('schemas/fixed')

    if update_json:
        shutil.rmtree('schemas/', ignore_errors=True)
        print("... Downloading JSON schema: please wait ...")
        download_schema(original_schema_path)
        print(f"Downloaded JSON schemas in {original_schema_path}")
        fix_schema(original_schema_path, fixed_schema_path)
        print(f"Fixed JSON schemas in {fixed_schema_path}")

    schema = get_python_schema(fixed_schema_path)

    returns = statham.schema.parser.parse(schema)
    returns_path = Path('toshling/models/return_types.py')
    returns_path.write_text(statham.serializers.python.serialize_python(*returns))
    print(f"Updated Returned types in {returns_path}")

    # Iterate the LDOs from all schemas, with the aim of
    # automatically discovering all API methods
    filtered_api_methods = filter_api_methods(get_api_methods(schema))
    # pprint.pprint(filtered_api_methods, sort_dicts=False)

    # Write the argument models Python module.
    sorted_filtered_api_methods = (
        value
        for key, value in sorted(filtered_api_methods.items(), key=lambda x: x[0][:-1])
    )
    arguments = (
        api_method['argument']
        for api_method in sorted_filtered_api_methods
        if api_method['argument']
    )
    arg_types_path = Path('toshling/models/argument_types.py')
    arg_types_content = statham.serializers.python.serialize_python(*arguments)  # type:ignore
    arg_types_path.write_text(arg_types_content)
    print(f"Updated Argument Types in {arg_types_path}")


    def key_sort_class_name(dict_class: Dict[str, Any]) -> List[str]:
        """Sort Classes alphabetically, with dependance on sub-classes"""
        crumbs = re.findall(r"[A-Z][a-z0-9]+", dict_class["name"])
        return crumbs if len(crumbs) > 1 else [crumbs[0], "zzz"]

    end_tmp = Path('_endpoints.py.j2')
    template = Template(end_tmp.read_text())
    end_out = Path('toshling/_endpoints.py')

    classes = get_classes(filtered_api_methods)
    classes_sorted = sorted(classes.values(), key=key_sort_class_name)
    end_out.write_text(template.render(classes=classes_sorted))
    print(f"Updated Endpoints in {end_out}")

    print("=> GENERATION SUCCESSFUL!")


if __name__ == "__main__":
    p = ArgumentParser(
        "toshling generator",
        description="Tool to update models and endpoints for Toshling"
    )
    p.add_argument(
        "--offline",
        action="store_true",
        help="Stay offline and used JSON files already downloaded"
    )
    options = p.parse_args()
    main(update_json=not options.offline)
