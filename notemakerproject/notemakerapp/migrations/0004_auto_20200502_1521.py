# Generated by Django 2.2.12 on 2020-05-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notemakerapp', '0003_auto_20200502_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
