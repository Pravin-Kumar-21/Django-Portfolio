# Generated by Django 5.0.1 on 2024-03-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0047_alter_projectphotos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectphotos',
            name='page_details',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projectphotos',
            name='Project_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Project_SS'),
        ),
    ]
