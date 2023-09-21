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
    id_kategori = models.ForeignKey(Satuan, on_delete=models.CASCADE)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE)
