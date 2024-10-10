from lib2to3.fixes.fix_input import context
from msilib.schema import ListView

from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like, Comment
from petstagram.photos.models import Photo


# Create your views here.


def home_page(request):
    photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        photos = photos.filter(
            tagged_pets__name__icontains=search_form.cleaned_data['pet_name'],
        )

    context = {
        'photos': photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context=context)


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


def add_comment(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

            return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
