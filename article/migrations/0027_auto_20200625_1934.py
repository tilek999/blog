# Generated by Django 3.0.7 on 2020-06-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0026_auto_20200623_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='articles/200625'),
        ),
    ]
