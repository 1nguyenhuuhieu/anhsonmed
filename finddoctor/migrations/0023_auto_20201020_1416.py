# Generated by Django 3.1.2 on 2020-10-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0022_auto_20201020_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='isstaff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=998201, null=True, unique=True),
        ),
    ]