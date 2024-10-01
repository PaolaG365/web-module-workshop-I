from django.contrib import admin
from petstagram.common.models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'date_time_of_publication', 'to_photo']