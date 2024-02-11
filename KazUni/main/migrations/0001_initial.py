# Generated by Django 5.0.1 on 2024-01-15 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currencys',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lil_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deal_Types',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group_deals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Cashs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Checks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Deals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CounterPartys',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('title', models.IntegerField()),
                ('full_title', models.CharField(max_length=250)),
                ('bincode', models.IntegerField()),
                ('main_cash', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.main_cashs')),
                ('main_deal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.main_deals')),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.parents')),
            ],
        ),
        migrations.CreateModel(
            name='TOO_GROUPS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('bincode', models.IntegerField()),
                ('full_name', models.CharField(max_length=50)),
                ('main_cash', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.main_cashs')),
                ('main_check', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.main_checks')),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('deal_num', models.IntegerField()),
                ('deal_date', models.DateField()),
                ('deal_start_date', models.DecimalField(decimal_places=10, max_digits=255)),
                ('deal_end_date', models.DecimalField(decimal_places=10, max_digits=225)),
                ('CounterParty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.counterpartys')),
                ('Currency', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.currencys')),
                ('deal_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.deal_types')),
                ('Group_deal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.group_deals')),
                ('TOO_GROUP', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.too_groups')),
            ],
        ),
    ]
