# Generated by Django 2.2.1 on 2019-05-30 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hw_21', '0008_framework_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Framework',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]