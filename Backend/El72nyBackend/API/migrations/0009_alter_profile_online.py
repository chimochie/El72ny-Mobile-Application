# Generated by Django 4.1.7 on 2023-06-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_hospital_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
