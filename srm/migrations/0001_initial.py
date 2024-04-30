# Generated by Django 5.0.4 on 2024-04-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                ("full_name", models.CharField(max_length=123)),
                ("email", models.EmailField(max_length=254)),
                (
                    "subject_line",
                    models.CharField(blank=True, max_length=123, null=True),
                ),
                ("message", models.TextField()),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Теплый"),
                            (2, "Горячий"),
                            (3, "Мертвый"),
                            (4, "Другое"),
                        ],
                        default=1,
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
