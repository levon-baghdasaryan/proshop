from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products


@api_view(['GET'])
def index(request):
    return Response(products)


@api_view(['GET'])
def show(request, id):
    product = None
    for item in products:
        if item['_id'] == id:
            product = item
            break

    return Response(product)
