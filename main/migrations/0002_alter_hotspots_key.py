# Generated by Django 4.1.6 on 2023-02-13 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotspots',
            name='key',
            field=models.CharField(max_length=1000),
        ),
    ]
