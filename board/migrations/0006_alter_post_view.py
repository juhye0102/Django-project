# Generated by Django 4.1.6 on 2023-02-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0005_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="view",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
