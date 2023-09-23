from rest_framework.viewsets import ModelViewSet
from ..models import Product
from ..serializers import ProductSerializer
from rest_framework.permissions import AllowAny


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('kategori', 'status').all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        data = Product.objects.select_related(
            'kategori', 'status')
        params = self.request.GET.get('status', None)
        if params:
            return data.filter(status__nama_status=params).all()
        return data.all()
