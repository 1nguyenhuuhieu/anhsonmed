# Generated by Django 3.1.2 on 2020-10-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0025_auto_20201021_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=339912, null=True, unique=True),
        ),
    ]
