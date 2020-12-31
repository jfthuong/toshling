from ..models.argument_types import *

_GENERATED_API_METHODS = \
{'accounts.create': {'argument': AccountsCreateArgument,
                     'href': '/accounts',
                     'method': 'POST',
                     'return': None},
 'accounts.delete': {'argument': AccountsDeleteArgument,
                     'href': '/accounts/{id}',
                     'method': 'DELETE',
                     'return': None},
 'accounts.force_delete': {'argument': AccountsForceDeleteArgument,
                           'href': '/accounts/{id}/force_delete',
                           'method': 'POST',
                           'return': None},
 'accounts.get': {'argument': AccountsGetArgument,
                  'href': '/accounts/{id}',
                  'method': 'GET',
                  'return': None},
 'accounts.list': {'argument': AccountsListArgument,
                   'href': '/accounts',
                   'method': 'GET',
                   'return': None},
 'accounts.merge': {'argument': AccountsMergeArgument,
                    'href': '/accounts/merge',
                    'method': 'POST',
                    'return': None},
 'accounts.move': {'argument': AccountsMoveArgument,
                   'href': '/accounts/{id}/move',
                   'method': 'POST',
                   'return': None},
 'accounts.reorder': {'argument': AccountsReorderArgument,
                      'href': '/accounts/reorder',
                      'method': 'POST',
                      'return': None},
 'accounts.update': {'argument': AccountsUpdateArgument,
                     'href': '/accounts/{id}',
                     'method': 'PUT',
                     'return': None},
 'budgets.create': {'argument': BudgetsCreateArgument,
                    'href': '/budgets',
                    'method': 'POST',
                    'return': None},
 'budgets.delete': {'argument': BudgetsDeleteArgument,
                    'href': '/budgets/{id}',
                    'method': 'DELETE',
                    'return': None},
 'budgets.get': {'argument': BudgetsGetArgument,
                 'href': '/budgets/{id}',
                 'method': 'GET',
                 'return': None},
 'budgets.history': {'argument': BudgetsHistoryArgument,
                     'href': '/budgets/{id}/history',
                     'method': 'GET',
                     'return': None},
 'budgets.list': {'argument': BudgetsListArgument,
                  'href': '/budgets',
                  'method': 'GET',
                  'return': None},
 'budgets.move': {'argument': BudgetsMoveArgument,
                  'href': '/budgets/{id}/move',
                  'method': 'POST',
                  'return': None},
 'budgets.reorder': {'argument': BudgetsReorderArgument,
                     'href': '/budgets/reorder',
                     'method': 'POST',
                     'return': None},
 'budgets.update': {'argument': BudgetsUpdateArgument,
                    'href': '/budgets/{id}',
                    'method': 'PUT',
                    'return': None},
 'categories.create': {'argument': CategoriesCreateArgument,
                       'href': '/categories',
                       'method': 'POST',
                       'return': None},
 'categories.delete': {'argument': CategoriesDeleteArgument,
                       'href': '/categories/{id}',
                       'method': 'DELETE',
                       'return': None},
 'categories.get': {'argument': CategoriesGetArgument,
                    'href': '/categories/{id}',
                    'method': 'GET',
                    'return': None},
 'categories.merge': {'argument': CategoriesMergeArgument,
                      'href': '/categories/merge',
                      'method': 'POST',
                      'return': None},
 'categories.sums.list': {'argument': CategoriesSumsListArgument,
                          'href': '/categories/sums',
                          'method': 'GET',
                          'return': None},
 'categories.update': {'argument': CategoriesUpdateArgument,
                       'href': '/categories/{id}',
                       'method': 'PUT',
                       'return': None},
 'currencies.list': {'argument': CurrenciesListArgument,
                     'href': '/currencies',
                     'method': 'GET',
                     'return': None},
 'entries.create': {'argument': EntriesCreateArgument,
                    'href': '/entries',
                    'method': 'POST',
                    'return': None},
 'entries.delete': {'argument': EntriesDeleteArgument,
                    'href': '/entries/{id}',
                    'method': 'DELETE',
                    'return': None},
 'entries.get': {'argument': EntriesGetArgument,
                 'href': '/entries/{id}',
                 'method': 'GET',
                 'return': None},
 'entries.list': {'argument': EntriesListArgument,
                  'href': '/entries',
                  'method': 'GET',
                  'return': None},
 'entries.locations.get': {'argument': EntriesLocationsGetArgument,
                           'href': '/entries/locations/{id}',
                           'method': 'GET',
                           'return': None},
 'entries.locations.list': {'argument': EntriesLocationsListArgument,
                            'href': '/entries/locations',
                            'method': 'GET',
                            'return': None},
 'entries.manage': {'argument': None,
                    'href': '/entries/manage',
                    'method': 'GET',
                    'return': None},
 'entries.repeats': {'argument': None,
                     'href': '/entries/repeats',
                     'method': 'GET',
                     'return': None},
 'entries.split': {'argument': EntriesSplitArgument,
                   'href': '/entries/split/{id}',
                   'method': 'DELETE',
                   'return': None},
 'entries.sums.list': {'argument': EntriesSumsListArgument,
                       'href': '/entries/sums',
                       'method': 'GET',
                       'return': None},
 'entries.update': {'argument': EntriesUpdateArgument,
                    'href': '/entries/{id}',
                    'method': 'PUT',
                    'return': None},
 'exports.create': {'argument': ExportsCreateArgument,
                    'href': '/exports',
                    'method': 'POST',
                    'return': None},
 'exports.get': {'argument': ExportsGetArgument,
                 'href': '/exports/{id}',
                 'method': 'GET',
                 'return': None},
 'exports.list': {'argument': ExportsListArgument,
                  'href': '/exports',
                  'method': 'GET',
                  'return': None},
 'exports.update': {'argument': ExportsUpdateArgument,
                    'href': '/exports/{id}',
                    'method': 'PUT',
                    'return': None},
 'images.create': {'argument': None,
                   'href': '/images',
                   'method': 'POST',
                   'return': None},
 'images.delete': {'argument': ImagesDeleteArgument,
                   'href': '/images/{id}',
                   'method': 'DELETE',
                   'return': None},
 'images.get': {'argument': ImagesGetArgument,
                'href': '/images/{id}',
                'method': 'GET',
                'return': None},
 'images.list': {'argument': ImagesListArgument,
                 'href': '/images',
                 'method': 'GET',
                 'return': None},
 'me.adjust.campaign': {'argument': MeAdjustCampaignArgument,
                        'href': '/me/adjust/campaign',
                        'method': 'POST',
                        'return': None},
 'me.devices': {'argument': None,
                'href': '/me/devices',
                'method': 'GET',
                'return': None},
 'me.get': {'argument': None, 'href': '/me', 'method': 'GET', 'return': None},
 'me.notifications.delete': {'argument': MeNotificationsDeleteArgument,
                             'href': '/me/notifications/{id}',
                             'method': 'DELETE',
                             'return': None},
 'me.notifications.dismiss_all': {'argument': None,
                                  'href': '/me/notifications/dismiss_all',
                                  'method': 'POST',
                                  'return': None},
 'me.notifications.get': {'argument': MeNotificationsGetArgument,
                          'href': '/me/notifications/{id}',
                          'method': 'GET',
                          'return': None},
 'me.notifications.list': {'argument': MeNotificationsListArgument,
                           'href': '/me/notifications',
                           'method': 'GET',
                           'return': None},
 'me.push': {'argument': MePushArgument,
             'href': '/me/push',
             'method': 'POST',
             'return': None},
 'me.revert': {'argument': MeRevertArgument,
               'href': '/me/revert',
               'method': 'POST',
               'return': None},
 'me.settings': {'argument': None,
                 'href': '/me/settings',
                 'method': 'GET',
                 'return': None},
 'me.update': {'argument': MeUpdateArgument,
               'href': '/me',
               'method': 'PUT',
               'return': None},
 'tags.create': {'argument': TagsCreateArgument,
                 'href': '/tags',
                 'method': 'POST',
                 'return': None},
 'tags.delete': {'argument': TagsDeleteArgument,
                 'href': '/tags/{id}',
                 'method': 'DELETE',
                 'return': None},
 'tags.get': {'argument': TagsGetArgument,
              'href': '/tags/{id}',
              'method': 'GET',
              'return': None},
 'tags.list': {'argument': TagsListArgument,
               'href': '/tags',
               'method': 'GET',
               'return': None},
 'tags.merge': {'argument': TagsMergeArgument,
                'href': '/tags/merge',
                'method': 'POST',
                'return': None},
 'tags.sums.list': {'argument': TagsSumsListArgument,
                    'href': '/tags/sums',
                    'method': 'GET',
                    'return': None},
 'tags.update': {'argument': TagsUpdateArgument,
                 'href': '/tags/{id}',
                 'method': 'PUT',
                 'return': None}}