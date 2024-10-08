# Generated by Django 5.0.7 on 2024-07-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to='cover_letters/'),
        ),
        migrations.AddField(
            model_name='job',
            name='portfolio',
            field=models.FileField(blank=True, null=True, upload_to='portfolios/'),
        ),
        migrations.AddField(
            model_name='job',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
