from rest_framework.viewsets import ModelViewSet
from ..models import Product
from ..serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('kategori', 'status').all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        data = Product.objects.select_related(
            'kategori', 'status')
        params = self.request.GET.get('status', None)
        print(params)
        if params:
            print(data.filter(status__nama_status=params).all())
            return data.filter(status__nama_status=params).all()
        print(params)
        return data.all()
