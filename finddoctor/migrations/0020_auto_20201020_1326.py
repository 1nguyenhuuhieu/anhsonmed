# Generated by Django 3.1.2 on 2020-10-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0019_auto_20201020_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='created',
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=106072, null=True, unique=True),
        ),
    ]
