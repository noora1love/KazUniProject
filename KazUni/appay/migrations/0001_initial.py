# Generated by Django 5.0.1 on 2024-01-28 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankcards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='countrypartyes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='typeofoperations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='typeofpays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ModelPays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=25000, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('dateofstart', models.DateField(blank=True, null=True)),
                ('dateofend', models.DateField(default=2005)),
                ('bankcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.bankcards')),
                ('countrparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.countrypartyes')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.organizations')),
                ('typeofoperation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.typeofoperations')),
                ('typeofpay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.typeofpays')),
            ],
        ),
    ]
