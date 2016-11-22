# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('codigo', models.CharField(max_length=7)),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='foto_venta')),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.DecimalField(null=True, decimal_places=1, blank=True, max_digits=3)),
                ('existencia', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('dpi', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=100)),
                ('productos', models.ManyToManyField(to='venta.Productos')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('dpi', models.CharField(max_length=9)),
                ('codigo', models.CharField(max_length=7)),
                ('cantidad', models.CharField(max_length=3)),
                ('fecha', models.DateField()),
                ('productos', models.ManyToManyField(to='venta.Productos')),
            ],
        ),
    ]
