# Generated by Django 3.0.7 on 2020-06-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0023_auto_20200620_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='articles/200622'),
        ),
    ]
