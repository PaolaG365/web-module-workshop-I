from django.shortcuts import render

from petstagram.pets.models import Pet


# Create your views here.
def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    photos = pet.tagged_pets.all()
    context = {
        'pet': pet,
        'photos': photos,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request):
    return render(request, 'pets/pet-edit-page.html')


def delete_pet(request):
    return render(request, 'pets/pet-delete-page.html')
