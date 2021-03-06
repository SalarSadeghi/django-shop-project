# Generated by Django 4.0.4 on 2022-05-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
