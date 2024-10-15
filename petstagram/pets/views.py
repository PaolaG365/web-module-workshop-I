from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
# def add_pet(request):
#     form = PetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1)
#
#     context = {'form': form}
#     return render(request, 'pets/pet-add-page.html', context)

# TODO: add functionality once user model is created
class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('details_acc', kwargs={'pk': 1})  # sample pk


# def details_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     photos = pet.tagged_pets.all()
#     comment_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'photos': photos,
#         'comment_form': comment_form,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class DetailsPetView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.tagged_pets.all()
        context['comment_form'] = CommentForm()

        return context


# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     if request.method == "GET":
#         form = PetForm(instance=pet)
#     else:
#         form = PetForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('details_pet', username, pet_slug)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy(
            'details_pet',
            kwargs = {
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug']
            }
        )


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     if request.method == "POST":
#         pet.delete()
#         return redirect('profile-details', pk=1)  # sample pk as i dont have user functionality yet
#
#     form = PetDeleteForm(initial=pet.__dict__)
#     context = {
#         'form': form,
#     }
#     return render(request, 'pets/pet-delete-page.html', context)


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('details_acc', kwargs={'pk': 1})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)
