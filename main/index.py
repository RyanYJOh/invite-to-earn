# Algolia setting

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Service, Invitation

@register(Service)
class ServiceIndex(AlgoliaIndex):
    fields = ('service_kr', 'service_en', 'verified')
    settings = {
        'searchableAttributes': ['service_kr', 'service_en'],
        'attributesForFaceting' : ['filterOnly(verified)']
        }
    index_name = 'dev_services'
    # index_name = 'prod_services'
