# Generated by Django 2.2.6 on 2019-10-12 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20191012_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyect',
            old_name='url',
            new_name='urlTo',
        ),
    ]
