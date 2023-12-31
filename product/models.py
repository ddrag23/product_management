from django.db import models
# Create your models here.


class Satuan(models.Model):
    id_satuan = models.AutoField(primary_key=True, unique=True, editable=False)
    nama_satuan = models.CharField(max_length=255)


class Status(models.Model):
    id_status = models.AutoField(primary_key=True, unique=True, editable=False)
    nama_status = models.CharField(max_length=255)


class Product(models.Model):
    id_product = models.IntegerField(primary_key=True)
    nomor = models.IntegerField(null=True)
    nama_product = models.CharField(max_length=255)
    harga = models.CharField()
    kategori = models.ForeignKey(
        to=Satuan, related_name="kategori", on_delete=models.CASCADE)
    status = models.ForeignKey(
        to=Status, related_name="status", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
