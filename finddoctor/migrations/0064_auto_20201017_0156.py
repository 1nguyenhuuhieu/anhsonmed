# Generated by Django 3.1.2 on 2020-10-17 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0063_auto_20201016_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=541076, null=True, unique=True),
        ),
    ]
