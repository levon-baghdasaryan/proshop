from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    return Response(products)


@api_view(['GET'])
def show(request, id):
    product = Product.objects.get(id=id)
    return Response(product)
