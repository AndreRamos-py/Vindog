# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-06-23 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racas', '0010_auto_20230623_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachorro',
            name='personalidade',
            field=models.CharField(choices=[('amigavel', 'Amigável'), ('inteligente', 'Inteligente'), ('afavel', 'Afável'), ('agressivo', 'Agressivo'), ('fiel', 'Fiel'), ('teimoso', 'Teimoso'), ('desajeitado', 'Desajeitado'), ('reservado', 'Reservado'), ('treinavel', 'Treinável')], default='amigavel', max_length=100),
        ),
    ]