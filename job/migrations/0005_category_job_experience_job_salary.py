# Generated by Django 4.0.3 on 2022-03-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_publinshed_at_job_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
