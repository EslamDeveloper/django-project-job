# Generated by Django 4.0.3 on 2022-03-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_remove_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]