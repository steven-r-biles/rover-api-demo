# Generated by Django 5.0.1 on 2024-01-23 03:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('accepted', models.BooleanField(default=False)),
                ('reject_reason', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField()),
                ('command', models.CharField(max_length=100)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rover.mission')),
            ],
        ),
    ]
