# Generated by Django 5.0.1 on 2024-01-15 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counterpartys',
            name='main_cash',
        ),
        migrations.RemoveField(
            model_name='counterpartys',
            name='main_deal',
        ),
        migrations.RemoveField(
            model_name='counterpartys',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='CounterParty',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='Currency',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='deal_type',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='Group_deal',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='TOO_GROUP',
        ),
        migrations.RemoveField(
            model_name='too_groups',
            name='main_cash',
        ),
        migrations.RemoveField(
            model_name='too_groups',
            name='main_check',
        ),
        migrations.DeleteModel(
            name='Main_Deals',
        ),
        migrations.DeleteModel(
            name='Parents',
        ),
        migrations.DeleteModel(
            name='CounterPartys',
        ),
        migrations.DeleteModel(
            name='Currencys',
        ),
        migrations.DeleteModel(
            name='Deal_Types',
        ),
        migrations.DeleteModel(
            name='Group_deals',
        ),
        migrations.DeleteModel(
            name='Deals',
        ),
        migrations.DeleteModel(
            name='Main_Cashs',
        ),
        migrations.DeleteModel(
            name='Main_Checks',
        ),
        migrations.DeleteModel(
            name='TOO_GROUPS',
        ),
    ]
