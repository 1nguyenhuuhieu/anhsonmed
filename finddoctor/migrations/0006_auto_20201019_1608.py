# Generated by Django 3.1.2 on 2020-10-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0005_auto_20201019_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=791673, null=True, unique=True),
        ),
    ]
