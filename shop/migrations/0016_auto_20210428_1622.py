# Generated by Django 3.0.3 on 2021-04-28 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0015_auto_20210428_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cleared', 'Cleared'), ('Delivered', 'Delivered')], default='Pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]