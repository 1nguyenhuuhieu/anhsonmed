# Generated by Django 3.1.2 on 2020-10-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0010_auto_20201019_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=308315, null=True, unique=True),
        ),
    ]
