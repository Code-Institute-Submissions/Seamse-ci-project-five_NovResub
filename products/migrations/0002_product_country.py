# Generated by Django 3.2 on 2022-09-04 12:01

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=254, null=True),
        ),
    ]
