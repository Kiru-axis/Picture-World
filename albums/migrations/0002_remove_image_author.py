# Generated by Django 3.2.5 on 2021-07-04 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='author',
        ),
    ]
