# Generated by Django 5.1.1 on 2024-10-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.CharField(default='not selected', max_length=30),
        ),
    ]
