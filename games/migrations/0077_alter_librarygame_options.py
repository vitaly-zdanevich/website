# Generated by Django 4.2.1 on 2024-02-13 13:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0076_remove_gamelibrary_games_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="librarygame",
            options={"ordering": ("slug",)},
        ),
    ]
