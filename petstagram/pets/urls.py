from django.conf.urls.static import static
from django.urls import include, path

from petstagram import settings
from petstagram.pets import views


urlpatterns = [
    path('add/', views.AddPetView.as_view(), name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.DetailsPetView.as_view(), name='details_pet'),
        path('edit/', views.EditPetView.as_view(), name='edit_pet'),
        path('delete/', views.DeletePetView.as_view(), name='delete_pet'),
    ]))
]
