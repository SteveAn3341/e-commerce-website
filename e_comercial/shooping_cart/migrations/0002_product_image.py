# Generated by Django 4.1.7 on 2023-03-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooping_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
    ]