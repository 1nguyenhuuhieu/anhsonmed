# Generated by Django 3.1.2 on 2020-10-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0046_auto_20201015_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=621646, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bookapartment',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=330820, null=True),
        ),
    ]
