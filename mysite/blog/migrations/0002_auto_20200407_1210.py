# Generated by Django 3.0.5 on 2020-04-07 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pblished_date',
            new_name='published_date',
        ),
    ]
