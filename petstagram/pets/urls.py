from django.conf.urls.static import static
from django.urls import include, path

from petstagram import settings
from petstagram.pets import views


urlpatterns = [
    path('add/', views.add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details_pet, name='details_pet'),
        path('edit/', views.edit_pet, name='edit_pet'),
        path('delete/', views.delete_pet, name='delete_pet'),
    ]))
]

if settings.DEBUG:  # pet photos dont load idk why at this point
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

