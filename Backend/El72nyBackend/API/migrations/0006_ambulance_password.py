# Generated by Django 4.1.7 on 2023-06-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_ambulance_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='password',
            field=models.CharField(default='password', max_length=20),
            preserve_default=False,
        ),
    ]
