# Generated by Django 4.1.7 on 2023-06-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_ambulance_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesthospital',
            name='userCase',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]