# Generated by Django 5.0.1 on 2024-03-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0034_alter_aboutme_achievements"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutme",
            name="Achievements",
            field=models.CharField(
                blank=True,
                help_text="eg: your achievements till date",
                max_length=200,
                null=True,
            ),
        ),
    ]
