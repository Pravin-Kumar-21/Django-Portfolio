# Generated by Django 5.0.1 on 2024-03-05 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0035_alter_aboutme_achievements'),
    ]

    operations = [
        migrations.CreateModel(
            name='achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achive_list', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='Achievements',
        ),
    ]