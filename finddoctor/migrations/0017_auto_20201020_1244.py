# Generated by Django 3.1.2 on 2020-10-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0016_auto_20201020_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=281907, null=True, unique=True),
        ),
    ]