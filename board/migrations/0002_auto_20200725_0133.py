# Generated by Django 3.0.8 on 2020-07-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publications",
            name="amount_of_upvotes",
            field=models.IntegerField(default=0, verbose_name="Количество голосов"),
        ),
    ]
