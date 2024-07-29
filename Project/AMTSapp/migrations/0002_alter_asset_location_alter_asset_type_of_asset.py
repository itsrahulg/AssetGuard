# Generated by Django 5.0.7 on 2024-07-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMTSapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='location',
            field=models.CharField(choices=[('isl_lab', 'ISL Lab'), ('cc_lab', 'CC Lab'), ('project_lab', 'Project Lab'), ('ibm_lab', 'IBM Lab'), ('g1_class_first_year', 'G1 Class First Year'), ('g1_class_second_year', 'G1 Class Second Year'), ('g2_class_first_year', 'G2 Class First Year'), ('g2_class_second_year', 'G2 Class Second Year'), ('wireless_communication_lab', 'Wireless Communication Laboratory')], max_length=50),
        ),
        migrations.AlterField(
            model_name='asset',
            name='type_of_asset',
            field=models.CharField(choices=[('hardware', 'Hardware'), ('software', 'Software'), ('furniture', 'Furniture'), ('book', 'Book'), ('other', 'Other')], max_length=50),
        ),
    ]
