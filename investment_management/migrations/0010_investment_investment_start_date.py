# Generated by Django 4.2.2 on 2023-08-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_management', '0009_investmentgroup_investment_investment_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='investment_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
