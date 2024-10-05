from lib2to3.fixes.fix_input import context
from msilib.schema import ListView

from django.shortcuts import render

from petstagram.photos.models import Photo


# Create your views here.


def home_page(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context=context)


# class HomePageView(ListView):
#     model = Photo
#     template_name = 'common/home-page.html'
#     context_object_name = 'photos'