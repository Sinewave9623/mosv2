# Generated by Django 3.2.16 on 2022-10-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20221031_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermaster',
            name='contactNo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customermaster',
            name='emailId',
            field=models.EmailField(blank=True, max_length=40, verbose_name='emailId address'),
        ),
        migrations.AlterField(
            model_name='membermaster',
            name='contactNo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
