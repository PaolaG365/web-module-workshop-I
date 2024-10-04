from django.urls import path, include
from petstagram.accounts import views


urlpatterns = [
    path('register/', views.register_acc, name='register'),
    path('login/', views.login_acc, name='login'),

    path('profile/<int:pk>/', include([
        path('', views.details_acc, name='details_acc'),
        path('edit/', views.edit_acc, name='edit_acc'),
        path('delete/', views.delete_acc, name='delete_acc'),
    ]))
]