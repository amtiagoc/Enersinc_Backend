# Generated by Django 4.0.6 on 2022-10-08 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_user_hobbie_alter_user_tipo_doc_delete_hobbie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='apellidos',
            new_name='surnames',
        ),
    ]
