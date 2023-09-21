from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product
from django.urls import reverse


def index(request: HttpRequest):
    return render(request, "main.html", {})


def store(request: HttpRequest):
    return render(request, "tambah.html")
