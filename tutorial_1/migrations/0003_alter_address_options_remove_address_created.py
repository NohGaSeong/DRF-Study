# Generated by Django 4.1.2 on 2022-10-13 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_1', '0002_rename_phonenumber_address_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.RemoveField(
            model_name='address',
            name='created',
        ),
    ]
