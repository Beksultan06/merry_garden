# Generated by Django 4.2.6 on 2023-10-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_photo', models.ImageField(upload_to='logo_image/', verbose_name='лучшиии фото')),
                ('photos', models.ImageField(upload_to='logo_image/', verbose_name='фото')),
            ],
            options={
                'verbose_name': ('Настройки галереи',),
                'verbose_name_plural': 'Настройка голорея',
            },
        ),
    ]