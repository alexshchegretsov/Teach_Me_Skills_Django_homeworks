# Generated by Django 2.2.1 on 2019-05-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cw_20', '0002_auto_20190523_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profession',
            field=models.CharField(max_length=200),
        ),
    ]