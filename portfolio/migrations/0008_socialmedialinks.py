# Generated by Django 5.0.1 on 2024-01-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_mycontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('social_icon', models.CharField(blank=True, max_length=60, null=True, verbose_name='Icon (eg: fa -fa-twitter)')),
            ],
            options={
                'verbose_name_plural': 'Hero section Social Media Links',
            },
        ),
    ]
