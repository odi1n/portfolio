# Generated by Django 3.2.9 on 2022-01-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Завершил обучение'),
        ),
    ]
