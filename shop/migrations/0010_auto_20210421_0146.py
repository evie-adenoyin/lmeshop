# Generated by Django 3.0.3 on 2021-04-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210421_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hall',
            field=models.CharField(choices=[('Abigail', 'Abigail'), ('Abraham', 'Abraham'), ('Daniel', 'Daniel'), ('Deborah', 'Deborah'), ('Dorcas', 'Dorcas'), ('Joseph', 'Joseph'), ('Isaac', 'Isaac'), ('Sarah', 'Sarah')], max_length=500, null=True),
        ),
    ]