# Generated by Django 5.1.5 on 2025-01-29 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teavarient',
            name='varienttype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='shop.tea'),
        ),
        migrations.AlterField(
            model_name='teavarient',
            name='varientname',
            field=models.CharField(max_length=255),
        ),
    ]
