# Generated by Django 3.0.3 on 2021-04-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_remove_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Hostel', max_length=200),
        ),
    ]
