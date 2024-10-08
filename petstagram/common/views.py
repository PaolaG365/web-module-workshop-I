from lib2to3.fixes.fix_input import context
from msilib.schema import ListView

from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import Like
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

def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    liked_obj = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_obj:
        liked_obj.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_REFERER'] + resolve_url('details_photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
