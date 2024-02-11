# Generated by Django 5.0.1 on 2024-02-10 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appay', '0005_departments_regpay_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='budgetitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1c', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=9, null=True)),
                ('name', models.CharField(max_length=50)),
                ('isgroup', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='countrypartyes',
            old_name='codeOKPO',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='countrypartyes',
            name='country',
        ),
        migrations.RemoveField(
            model_name='countrypartyes',
            name='numberofregistration',
        ),
        migrations.RemoveField(
            model_name='countrypartyes',
            name='parentcountryparty',
        ),
        migrations.RemoveField(
            model_name='countrypartyes',
            name='region',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='VATagent',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='activityagreement',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='countrypartyes',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='groupdeal',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='typeofdeal',
        ),
        migrations.AddField(
            model_name='countrypartyes',
            name='id1c',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deals',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deals',
            name='id1c',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deals',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appay.countrypartyes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelpays',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appay.currencyes'),
        ),
        migrations.AddField(
            model_name='modelpays',
            name='id1c',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='modelpays',
            name='numberofdocument',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organizations',
            name='bin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organizations',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='organizations',
            name='id1c',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='moneyresources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1c', models.CharField(max_length=50)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('numberofcheck', models.CharField(blank=True, max_length=50, null=True)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appay.banks')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appay.currencyes')),
                ('typeofpay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.typeofpays')),
            ],
        ),
        migrations.AddField(
            model_name='modelpays',
            name='moneyresource',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appay.moneyresources'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1c', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('isgroup', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.budgetitems')),
            ],
        ),
        migrations.CreateModel(
            name='TableModelPays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberofline', models.IntegerField(blank=True, null=True)),
                ('paymentamount', models.IntegerField(blank=True, null=True)),
                ('budgetitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.budgetitems')),
                ('dealofcountrparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.deals')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appay.projects')),
            ],
        ),
    ]
