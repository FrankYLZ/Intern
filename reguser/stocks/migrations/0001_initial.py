# Generated by Django 4.2.1 on 2023-05-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stock",
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
                ("date", models.DateField()),
                ("timezone", models.CharField(max_length=50)),
                ("stock_symbol", models.CharField(max_length=10)),
                ("predicted_price", models.FloatField()),
                ("currency", models.CharField(max_length=10)),
            ],
        ),
    ]
