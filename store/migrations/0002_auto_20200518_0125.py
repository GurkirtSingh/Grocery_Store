# Generated by Django 3.0.3 on 2020-05-18 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='createdDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]