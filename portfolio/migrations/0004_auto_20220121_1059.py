# Generated by Django 3.2.9 on 2022-01-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_experience_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='employment',
            field=models.CharField(blank=True, help_text='Например: полная, неполная, и тд.', max_length=255, null=True, verbose_name='Занятость'),
        ),
        migrations.AlterField(
            model_name='work',
            name='post',
            field=models.CharField(blank=True, help_text='Например: Backend, Frontend, ...', max_length=255, null=True, verbose_name='Желаемая должность'),
        ),
        migrations.AlterField(
            model_name='work',
            name='salary',
            field=models.IntegerField(blank=True, default=0, help_text='Например: 100000', null=True, verbose_name='Желаемая зарплата'),
        ),
        migrations.AlterField(
            model_name='work',
            name='travel_time',
            field=models.CharField(blank=True, help_text='Например: не имеет значение', max_length=255, null=True, verbose_name='Время в пути'),
        ),
    ]
