# Generated by Django 3.2.9 on 2021-12-29 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['portfolio', 'project__title'], 'verbose_name': 'Опыт', 'verbose_name_plural': 'Опыт'},
        ),
    ]
