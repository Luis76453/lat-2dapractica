# Generated by Django 4.2.7 on 2023-12-23 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0002_meseros_procedencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meseros',
            name='procedencia',
        ),
    ]
