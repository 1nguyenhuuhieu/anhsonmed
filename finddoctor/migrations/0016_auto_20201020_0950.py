# Generated by Django 3.1.1 on 2020-10-20 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0015_auto_20201020_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=929910, null=True, unique=True),
        ),
    ]
