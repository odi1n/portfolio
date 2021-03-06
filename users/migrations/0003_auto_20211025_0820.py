# Generated by Django 3.2.8 on 2021-10-25 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211025_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.languagetype', verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='social',
            name='social_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.socialtype', verbose_name='Тип соц.'),
        ),
    ]
