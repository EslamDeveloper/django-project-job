# Generated by Django 4.0.3 on 2022-03-23 22:49

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_job_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='salary',
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]