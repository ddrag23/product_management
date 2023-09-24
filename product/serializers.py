from rest_framework import serializers
from .models import Product, Satuan, Status


class ProductSerializer(serializers.ModelSerializer):
    kategori_id = serializers.ChoiceField(choices=[])
    status_id = serializers.ChoiceField(choices=[])
    kategori = serializers.CharField(
        source='kategori.nama_satuan', read_only=True)
    status = serializers.CharField(source="status.nama_status", read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fetch choices from the database and populate the ChoiceField choices
        self.fields['kategori_id'].choices = [
            (item.id_satuan, item.nama_satuan) for item in Satuan.objects.all()]
        self.fields['status_id'].choices = [
            (item.id_status, item.nama_status) for item in Status.objects.all()]

    class Meta:
        model = Product
        fields = '__all__'
