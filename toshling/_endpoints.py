from .models import argument_types, return_types


class Endpoint:
    def __init__(self, client):
        self.client = client

class Accounts(Endpoint):
    def create(self, **kwargs):
        return self.client.request('/accounts', 'POST', argument_type=argument_types.AccountsCreateArgument, **kwargs)
    
    def delete(self, **kwargs):
        return self.client.request('/accounts/{id}', 'DELETE', argument_type=argument_types.AccountsDeleteArgument, **kwargs)
    
    def force_delete(self, **kwargs):
        return self.client.request('/accounts/{id}/force_delete', 'POST', argument_type=argument_types.AccountsForceDeleteArgument, **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/accounts/{id}', 'GET', argument_type=argument_types.AccountsGetArgument, return_type=return_types.Account, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/accounts', 'GET', argument_type=argument_types.AccountsListArgument, return_type=return_types.Account, **kwargs)
    
    def merge(self, **kwargs):
        return self.client.request('/accounts/merge', 'POST', argument_type=argument_types.AccountsMergeArgument, **kwargs)
    
    def move(self, **kwargs):
        return self.client.request('/accounts/{id}/move', 'POST', argument_type=argument_types.AccountsMoveArgument, **kwargs)
    
    def reorder(self, **kwargs):
        return self.client.request('/accounts/reorder', 'POST', argument_type=argument_types.AccountsReorderArgument, **kwargs)
    
    def update(self, **kwargs):
        return self.client.request('/accounts/{id}', 'PUT', argument_type=argument_types.AccountsUpdateArgument, return_type=return_types.Account, **kwargs)
    

class Budgets(Endpoint):
    def create(self, **kwargs):
        return self.client.request('/budgets', 'POST', argument_type=argument_types.BudgetsCreateArgument, **kwargs)
    
    def delete(self, **kwargs):
        return self.client.request('/budgets/{id}', 'DELETE', argument_type=argument_types.BudgetsDeleteArgument, **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/budgets/{id}', 'GET', argument_type=argument_types.BudgetsGetArgument, return_type=return_types.Budget, **kwargs)
    
    def history(self, **kwargs):
        return self.client.request('/budgets/{id}/history', 'GET', argument_type=argument_types.BudgetsHistoryArgument, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/budgets', 'GET', argument_type=argument_types.BudgetsListArgument, return_type=return_types.Budget, **kwargs)
    
    def move(self, **kwargs):
        return self.client.request('/budgets/{id}/move', 'POST', argument_type=argument_types.BudgetsMoveArgument, **kwargs)
    
    def reorder(self, **kwargs):
        return self.client.request('/budgets/reorder', 'POST', argument_type=argument_types.BudgetsReorderArgument, **kwargs)
    
    def update(self, **kwargs):
        return self.client.request('/budgets/{id}', 'PUT', argument_type=argument_types.BudgetsUpdateArgument, return_type=return_types.Budget, **kwargs)
    

class CategoriesSums(Endpoint):
    def list(self, **kwargs):
        return self.client.request('/categories/sums', 'GET', argument_type=argument_types.CategoriesSumsListArgument, return_type=return_types.CategorySum, **kwargs)
    

class Categories(Endpoint):
    def __init__(self, client):
        super().__init__(client)
        self.sums = CategoriesSums(client)
    
    def create(self, **kwargs):
        return self.client.request('/categories', 'POST', argument_type=argument_types.CategoriesCreateArgument, **kwargs)
    
    def delete(self, **kwargs):
        return self.client.request('/categories/{id}', 'DELETE', argument_type=argument_types.CategoriesDeleteArgument, **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/categories/{id}', 'GET', argument_type=argument_types.CategoriesGetArgument, return_type=return_types.Category, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/categories', 'GET', argument_type=argument_types.CategoriesListArgument, return_type=return_types.Category, **kwargs)
    
    def merge(self, **kwargs):
        return self.client.request('/categories/merge', 'POST', argument_type=argument_types.CategoriesMergeArgument, **kwargs)
    
    def update(self, **kwargs):
        return self.client.request('/categories/{id}', 'PUT', argument_type=argument_types.CategoriesUpdateArgument, return_type=return_types.Category, **kwargs)
    

class Currencies(Endpoint):
    def list(self, **kwargs):
        return self.client.request('/currencies', 'GET', argument_type=argument_types.CurrenciesListArgument, return_type=return_types.CurrencyElement, **kwargs)
    

class EntriesLocations(Endpoint):
    def get(self, **kwargs):
        return self.client.request('/entries/locations/{id}', 'GET', argument_type=argument_types.EntriesLocationsGetArgument, return_type=return_types.Location, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/entries/locations', 'GET', argument_type=argument_types.EntriesLocationsListArgument, return_type=return_types.Location, **kwargs)
    

class EntriesSums(Endpoint):
    def list(self, **kwargs):
        return self.client.request('/entries/sums', 'GET', argument_type=argument_types.EntriesSumsListArgument, return_type=return_types.Day, **kwargs)
    

class Entries(Endpoint):
    def __init__(self, client):
        super().__init__(client)
        self.locations = EntriesLocations(client)
        self.sums = EntriesSums(client)
    
    def create(self, **kwargs):
        return self.client.request('/entries', 'POST', argument_type=argument_types.EntriesCreateArgument, **kwargs)
    
    def delete(self, **kwargs):
        return self.client.request('/entries/{id}', 'DELETE', argument_type=argument_types.EntriesDeleteArgument, **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/entries/{id}', 'GET', argument_type=argument_types.EntriesGetArgument, return_type=return_types.Entry, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/entries', 'GET', argument_type=argument_types.EntriesListArgument, return_type=return_types.Entry, **kwargs)
    
    def manage(self, **kwargs):
        return self.client.request('/entries/manage', 'GET', **kwargs)
    
    def repeats(self, **kwargs):
        return self.client.request('/entries/repeats', 'GET', **kwargs)
    
    def split(self, **kwargs):
        return self.client.request('/entries/split/{id}', 'DELETE', argument_type=argument_types.EntriesSplitArgument, **kwargs)
    
    def update(self, **kwargs):
        return self.client.request('/entries/{id}', 'PUT', argument_type=argument_types.EntriesUpdateArgument, return_type=return_types.Entry, **kwargs)
    

class Exports(Endpoint):
    def create(self, **kwargs):
        return self.client.request('/exports', 'POST', argument_type=argument_types.ExportsCreateArgument, **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/exports/{id}', 'GET', argument_type=argument_types.ExportsGetArgument, return_type=return_types.Export, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/exports', 'GET', argument_type=argument_types.ExportsListArgument, return_type=return_types.Export, **kwargs)
    
    def update(self, **kwargs):
        return self.client.request('/exports/{id}', 'PUT', argument_type=argument_types.ExportsUpdateArgument, return_type=return_types.Export, **kwargs)
    

class Images(Endpoint):
    def create(self, **kwargs):
        return self.client.request('/images', 'POST', **kwargs)
    
    def delete(self, **kwargs):
        return self.client.request('/images/{id}', 'DELETE', argument_type=argument_types.ImagesDeleteArgument, **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/images/{id}', 'GET', argument_type=argument_types.ImagesGetArgument, return_type=return_types.Image, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/images', 'GET', argument_type=argument_types.ImagesListArgument, return_type=return_types.Image, **kwargs)
    

class MeAdjust(Endpoint):
    def campaign(self, **kwargs):
        return self.client.request('/me/adjust/campaign', 'POST', argument_type=argument_types.MeAdjustCampaignArgument, **kwargs)
    

class MeNotifications(Endpoint):
    def delete(self, **kwargs):
        return self.client.request('/me/notifications/{id}', 'DELETE', argument_type=argument_types.MeNotificationsDeleteArgument, **kwargs)
    
    def dismiss_all(self, **kwargs):
        return self.client.request('/me/notifications/dismiss_all', 'POST', **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/me/notifications/{id}', 'GET', argument_type=argument_types.MeNotificationsGetArgument, return_type=return_types.Notification, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/me/notifications', 'GET', argument_type=argument_types.MeNotificationsListArgument, return_type=return_types.Notification, **kwargs)
    

class Me(Endpoint):
    def __init__(self, client):
        super().__init__(client)
        self.adjust = MeAdjust(client)
        self.notifications = MeNotifications(client)
    
    def devices(self, **kwargs):
        return self.client.request('/me/devices', 'GET', **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/me', 'GET', return_type=return_types.User, **kwargs)
    
    def push(self, **kwargs):
        return self.client.request('/me/push', 'POST', argument_type=argument_types.MePushArgument, **kwargs)
    
    def revert(self, **kwargs):
        return self.client.request('/me/revert', 'POST', argument_type=argument_types.MeRevertArgument, **kwargs)
    
    def settings(self, **kwargs):
        return self.client.request('/me/settings', 'GET', **kwargs)
    
    def update(self, **kwargs):
        return self.client.request('/me', 'PUT', argument_type=argument_types.MeUpdateArgument, return_type=return_types.User, **kwargs)
    

class TagsSums(Endpoint):
    def list(self, **kwargs):
        return self.client.request('/tags/sums', 'GET', argument_type=argument_types.TagsSumsListArgument, return_type=return_types.TagSum, **kwargs)
    

class Tags(Endpoint):
    def __init__(self, client):
        super().__init__(client)
        self.sums = TagsSums(client)
    
    def create(self, **kwargs):
        return self.client.request('/tags', 'POST', argument_type=argument_types.TagsCreateArgument, **kwargs)
    
    def delete(self, **kwargs):
        return self.client.request('/tags/{id}', 'DELETE', argument_type=argument_types.TagsDeleteArgument, **kwargs)
    
    def get(self, **kwargs):
        return self.client.request('/tags/{id}', 'GET', argument_type=argument_types.TagsGetArgument, return_type=return_types.Tag, **kwargs)
    
    def list(self, **kwargs):
        return self.client.request('/tags', 'GET', argument_type=argument_types.TagsListArgument, return_type=return_types.Tag, **kwargs)
    
    def merge(self, **kwargs):
        return self.client.request('/tags/merge', 'POST', argument_type=argument_types.TagsMergeArgument, **kwargs)
    
    def update(self, **kwargs):
        return self.client.request('/tags/{id}', 'PUT', argument_type=argument_types.TagsUpdateArgument, return_type=return_types.Tag, **kwargs)
    