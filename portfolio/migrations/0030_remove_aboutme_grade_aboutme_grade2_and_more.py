# Generated by Django 5.0.1 on 2024-03-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0029_alter_aboutme_grade_col'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='grade',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='grade2',
            field=models.IntegerField(blank=True, help_text='eg:', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='grade1',
            field=models.IntegerField(blank=True, help_text='eg: 77.6%', max_length=50),
        ),
    ]
