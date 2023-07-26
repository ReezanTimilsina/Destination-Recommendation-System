# Generated by Django 3.2.10 on 2022-02-09 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0008_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place_rating',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]