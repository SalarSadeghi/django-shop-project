# Generated by Django 4.0.4 on 2022-05-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(height_field=720, upload_to='images', width_field=720),
        ),
    ]
