from django.shortcuts import render
from .models import Car

# Create your views here.


def index(request):
    cars = Car.objects.all()
    cloudinary_img = {'cars': cars}
    return render(request, 'index.html', cloudinary_img)
