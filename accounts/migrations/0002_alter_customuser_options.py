# Generated by Django 5.0.4 on 2024-05-15 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('view_user', 'Can view user'), ('edit_user', 'Can edit user'), ('delete_user', 'Can delete user'), ('approve_user', 'Can approve user'))},
        ),
    ]
