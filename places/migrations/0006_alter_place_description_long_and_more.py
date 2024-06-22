# Generated by Django 4.2.13 on 2024-06-16 09:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0005_alter_image_options_alter_image__order_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=tinymce.models.HTMLField(blank=True, verbose_name="Длинное описание"),
        ),
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.CharField(max_length=255, verbose_name="Короткое описание"),
        ),
        migrations.AlterField(
            model_name="place",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
    ]