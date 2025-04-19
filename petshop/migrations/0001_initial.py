# Generated by Django 5.2 on 2025-04-12 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kakao_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('url', models.URLField(blank=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='petshop.hospital')),
            ],
        ),
    ]
