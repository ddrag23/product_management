from django.shortcuts import render
from django.http import HttpRequest
from .models import Satuan, Status


def index(request: HttpRequest):
    satuan = Satuan.objects.all()
    status = Status.objects.all()
    return render(request, "main.html", {'satuan': satuan, 'status': status})


def store(request: HttpRequest):
    return render(request, "tambah.html")
