# Generated by Django 5.0.4 on 2024-04-26 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_house_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Storage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "В процессе"), (2, "Одобрено")], default=1
                    ),
                ),
                (
                    "house",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.house"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
