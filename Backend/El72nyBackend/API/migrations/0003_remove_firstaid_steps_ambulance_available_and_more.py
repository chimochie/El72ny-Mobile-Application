# Generated by Django 4.1.7 on 2023-05-31 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_remove_profile_lat_remove_profile_lng_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstaid',
            name='steps',
        ),
        migrations.AddField(
            model_name='ambulance',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firstaid',
            name='Description',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='firstaid',
            name='stepNum',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='firstaid',
            name='video',
            field=models.FileField(null=True, upload_to='video'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctorId',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='profile',
            name='specialization',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='userId',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.DeleteModel(
            name='CheckupForm',
        ),
    ]