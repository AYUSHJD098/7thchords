# Generated by Django 3.1 on 2020-08-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_customer_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Message',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
