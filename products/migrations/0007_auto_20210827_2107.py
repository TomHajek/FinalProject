# Generated by Django 3.2.6 on 2021-08-27 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210814_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'ProductCategories'},
        ),
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'verbose_name_plural': 'ProductSubCategories'},
        ),
    ]
