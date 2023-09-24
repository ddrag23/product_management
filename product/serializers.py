from rest_framework import serializers
from .models import Product, Satuan, Status


class ProductSerializer(serializers.ModelSerializer):
    kategori_id = serializers.ChoiceField(
        choices=[(item.id_satuan, item.nama_satuan) for item in Satuan.objects.all()] if Satuan.objects.exists() else [])
    status_id = serializers.ChoiceField(
        choices=[(item.id_status, item.nama_status) for item in Status.objects.all()] if Satuan.objects.exists() else [])
    kategori = serializers.CharField(
        source='kategori.nama_satuan', read_only=True)
    status = serializers.CharField(source="status.nama_status", read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
