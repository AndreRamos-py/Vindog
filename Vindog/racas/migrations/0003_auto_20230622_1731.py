# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-06-22 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racas', '0002_auto_20230622_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cachorro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], default='M', max_length=1)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='raca',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='raca',
            name='sexo',
        ),
        migrations.AddField(
            model_name='raca',
            name='cores',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='raca',
            name='pais',
            field=models.CharField(default='', max_length=100),
        ),
    ]