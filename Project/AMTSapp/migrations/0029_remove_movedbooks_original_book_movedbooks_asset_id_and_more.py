# Generated by Django 5.0.7 on 2024-10-02 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMTSapp', '0028_alter_movedbooks_new_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movedbooks',
            name='original_book',
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='ASSET_ID',
            field=models.CharField(default='TEMP_ID', max_length=50),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='account_head',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='date_of_purchase',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='edition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='publishing_house',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='stock_register_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movedbooks',
            name='type_of_asset',
            field=models.CharField(default='Book', max_length=50),
        ),
    ]
