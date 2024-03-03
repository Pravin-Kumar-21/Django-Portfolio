# Generated by Django 5.0.1 on 2024-03-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_remove_aboutme_hire_me_userdetails_hire_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='hire_me',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='hire_me',
            field=models.CharField(default='Hire Me', max_length=255),
        ),
    ]