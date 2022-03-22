# Generated by Django 4.0 on 2022-03-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Suppliers', '0002_rename_businessidentity_suppliercompany_businessidentityno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliersaccount',
            name='first_name',
            field=models.CharField(default='Default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suppliersaccount',
            name='last_name',
            field=models.CharField(default='Default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suppliersaccount',
            name='phone_number',
            field=models.CharField(default='Default', max_length=50),
            preserve_default=False,
        ),
    ]
