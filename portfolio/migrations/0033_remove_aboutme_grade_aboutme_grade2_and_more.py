# Generated by Django 5.0.1 on 2024-03-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0032_remove_aboutme_grade2_aboutme_grade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='grade',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='grade2',
            field=models.CharField(blank=True, help_text='eg:', max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='grade1',
            field=models.CharField(blank=True, help_text='eg: 77.6%', max_length=50),
        ),
    ]
