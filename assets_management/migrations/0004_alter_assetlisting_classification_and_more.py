# Generated by Django 4.2.14 on 2024-08-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_management', '0003_assetlisting_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetlisting',
            name='classification',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='assetlisting',
            name='classification_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
