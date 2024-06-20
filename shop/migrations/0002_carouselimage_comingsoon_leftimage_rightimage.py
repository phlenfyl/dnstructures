# Generated by Django 5.0.2 on 2024-06-19 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Carousel Image',
                'verbose_name_plural': 'Carousel Images',
            },
        ),
        migrations.CreateModel(
            name='ComingSoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='commingsoon')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carouselsoon', to='shop.carouselimage')),
            ],
            options={
                'verbose_name': 'Coming Soon',
                'verbose_name_plural': 'Coming Soon',
            },
        ),
        migrations.CreateModel(
            name='LeftImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='leftimages')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carouselleft', to='shop.carouselimage')),
            ],
            options={
                'verbose_name': 'Left Image',
                'verbose_name_plural': 'Left Images',
            },
        ),
        migrations.CreateModel(
            name='RightImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='rightimages')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carouselright', to='shop.carouselimage')),
            ],
            options={
                'verbose_name': 'Right Image',
                'verbose_name_plural': 'Right Images',
            },
        ),
    ]
