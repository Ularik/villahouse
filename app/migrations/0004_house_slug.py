# Generated by Django 5.0.4 on 2024-04-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_storage"),
    ]

    operations = [
        migrations.AddField(
            model_name="house",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
