# Generated by Django 3.0.7 on 2020-06-18 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_auto_20200618_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['user'], 'verbose_name': 'коментарий', 'verbose_name_plural': 'коментарии'},
        ),
    ]
