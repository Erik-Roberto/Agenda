# Generated by Django 4.0.5 on 2022-06-21 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_mostrat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='mostrat',
            new_name='mostrar',
        ),
    ]
