# Generated by Django 4.1.2 on 2022-10-27 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('update_dt',)},
        ),
    ]