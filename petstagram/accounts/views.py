from django.shortcuts import render

# Create your views here.

def register_acc(request):
    return render(request, 'accounts/register-page.html')


def login_acc(request):
    return render(request, 'accounts/login-page.html')


def details_acc(request):
    return render(request, 'accounts/profile-details-page.html')


def edit_acc(request):
    return render(request, 'accounts/profile-edit-page.html')


def delete_acc(request):
    return render(request, 'accounts/profile-delete-page.html')
