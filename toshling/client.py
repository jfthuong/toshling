from . import endpoints
import requests
import json
from statham.schema.elements import Object
from statham.schema.constants import NotPassed


class StathamJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Object):
            return {type(o).properties[k].source: v for k, v in o._dict.items() if not isinstance(v, NotPassed)}
        
        return json.JSONEncoder.default(self, o)


class Client:
    def __init__(self, api_key, api_endpoint_base='https://api2.toshl.com'):
        self.api_key = api_key
        self.api_endpoint_base = api_endpoint_base

        self.accounts = endpoints.Accounts(self)
        self.budgets = endpoints.Budgets(self)
        self.categories = endpoints.Categories(self)
        self.currencies = endpoints.Currencies(self)
        self.entries = endpoints.Entries(self)
        self.exports = endpoints.Exports(self)
        self.images = endpoints.Images(self)
        self.me = endpoints.Me(self)
        self.tags = endpoints.Tags(self)
    
    def request(self, href, method, argument_type=None, return_type=None, **kwargs):
        options = {}
        if argument_type:
            remap = {}
            for k, v in kwargs.items():
                remap[argument_type.properties[k].source] = v
            if method == 'GET':
                options['params'] = remap
            else:
                options['data'] = json.dumps(argument_type(remap), cls=StathamJSONEncoder)
                options['headers'] = {'Content-Type': 'application/json'}
        print(options)
        response = requests.request(method,
                                    self.api_endpoint_base + href.format(**kwargs),
                                    auth=(self.api_key, ''),
                                    **options)
        if response.ok:
            if return_type:
                plain = response.json()
                if isinstance(plain, list):
                    return [return_type(p) for p in plain]
                else:
                    return return_type(response.json())
        else:
            response.raise_for_status()