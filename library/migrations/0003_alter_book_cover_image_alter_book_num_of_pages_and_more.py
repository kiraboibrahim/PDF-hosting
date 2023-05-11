# Generated by Django 4.1.7 on 2023-04-05 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0002_alter_bookcategory_options_book_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(editable=False, upload_to=library.models.book_cover_image_upload_path),
        ),
        migrations.AlterField(
            model_name='book',
            name='num_of_pages',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='uploader',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]