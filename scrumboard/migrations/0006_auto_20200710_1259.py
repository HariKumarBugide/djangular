# Generated by Django 3.0.5 on 2020-07-10 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0005_card_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='list',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
