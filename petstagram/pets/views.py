from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)  # TODO: add functionality once user model is created

    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    photos = pet.tagged_pets.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'photos': photos,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == "GET":
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details_pet', username, pet_slug)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect('profile-details', pk=1)  # sample pk as i dont have user functionality yet

    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-delete-page.html', context)
