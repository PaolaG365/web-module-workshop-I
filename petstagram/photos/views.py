from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from petstagram.photos.models import Photo


# Create your views here.

def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def details_photo(request, photo_pk):
    photo_obj = Photo.objects.filter(pk=photo_pk).first()
    likes = photo_obj.likes_photo.all()
    comments = photo_obj.comments_photo.all()

    if photo_obj:
        context = {
            'photo_obj': photo_obj,
            'likes': likes,
            'comments': comments
        }

        return render(request, 'photos/photo-details-page.html', context)

    return render(request, 'common/home-page.html')


def edit_photo(request):
    return render(request, 'photos/photo-edit-page.html')