# Generated by Django 5.0.7 on 2024-10-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMTSapp', '0033_projectorupdatelog_logged_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookupdatelog',
            name='logged_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookupdatelog',
            name='updated_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
