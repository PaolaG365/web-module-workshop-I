from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
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

    if request.method == 'POST':
        if search_form.is_valid():
            photos = photos.filter(
                tagged_pets__name__icontains=search_form.cleaned_data['pet_name'],
            )

    photos_per_page = 1
    paginator = Paginator(photos, photos_per_page)
    page = request.GET.get('page')

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = {
        'photos': photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context=context)


class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'photos'
    paginate_by = 2

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(** kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)

        return queryset


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
