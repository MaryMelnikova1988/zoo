# Generated by Django 5.0.1 on 2024-01-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Кличка')),
                ('category', models.CharField(max_length=100, verbose_name='Порода')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='Фото')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'собака',
                'verbose_name_plural': 'собаки',
            },
        ),
    ]