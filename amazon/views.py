import json

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from sp_api.api import Reports, Products, Catalog
from rest_framework.response import Response
from django.conf import settings

class CatalogViews(APIView):

    # renderer_classes = (JSONRenderer, )

    def get(self, request):
        response = Catalog(credentials=settings.SPAPI_CRIDENTIALS).get_item('ASIN_200', MarketplaceId='TEST_CASE_200')

        response_dict = {
            'payload': response.payload,
            # 'errors': response.errors,
            # 'pagination': response.pagination,
            # 'headers': response.headers,
            # 'nextToken': response.next_token
        }

        return Response({
            'data': json.dumps(response_dict)
        })

