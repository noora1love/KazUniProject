# Generated by Django 5.0.1 on 2024-02-11 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appay', '0006_budgetitems_rename_codeokpo_countrypartyes_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelpays',
            name='moneyresource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appay.moneyresources'),
        ),
    ]
