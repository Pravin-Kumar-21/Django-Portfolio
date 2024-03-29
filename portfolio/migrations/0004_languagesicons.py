# Generated by Django 5.0.1 on 2024-01-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_aboutme_description_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguagesIcons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=100, verbose_name='language Icon Image:(icons8.com)')),
                ('lang_name', models.CharField(blank=True, max_length=100, verbose_name='Language Name')),
                ('exp_level', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Junior', 'Junior'), ('Intermediate', 'Intermediate'), ('Experienced', 'Experienced')], max_length=200, verbose_name='Experience Level')),
            ],
            options={
                'verbose_name_plural': 'Skills section',
            },
        ),
    ]
