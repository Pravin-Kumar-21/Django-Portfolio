# Generated by Django 5.0.1 on 2024-03-05 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0039_remove_aboutme_achievements_aboutme_achievement1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='Achievement1',
            new_name='Achievements',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='Achievement2',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='Achievement3',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='Achievement4',
        ),
    ]
