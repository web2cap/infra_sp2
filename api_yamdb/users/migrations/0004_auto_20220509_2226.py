# Generated by Django 2.2.16 on 2022-05-09 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220509_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['role', 'username'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
