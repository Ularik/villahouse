# Generated by Django 5.0.4 on 2024-04-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="phone_number",
            field=models.CharField(max_length=13),
        ),
    ]
