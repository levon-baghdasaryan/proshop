from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Product
from ..serializers import ProductSerializer


@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def show(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
