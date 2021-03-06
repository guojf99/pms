# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('instruction_file', models.FileField(upload_to=products.models.get_file_path)),
                ('active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('business_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.BusinessCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductType'),
        ),
    ]
