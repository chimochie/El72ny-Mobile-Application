# Generated by Django 4.1.7 on 2023-06-07 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_hospital_alter_ambulance_available_requesthospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='hospital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='API.hospital'),
            preserve_default=False,
        ),
    ]
