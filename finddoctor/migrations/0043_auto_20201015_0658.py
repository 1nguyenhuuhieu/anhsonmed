# Generated by Django 3.1.1 on 2020-10-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0042_auto_20201014_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=204846, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bookapartment',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=529217, null=True),
        ),
    ]