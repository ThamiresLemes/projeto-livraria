# Generated by Django 3.2.8 on 2021-11-08 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_auto_20211107_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='data_cadastro',
            new_name='data_publicacao',
        ),
    ]