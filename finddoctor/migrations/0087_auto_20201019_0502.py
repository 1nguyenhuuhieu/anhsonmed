# Generated by Django 3.1.2 on 2020-10-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0086_auto_20201019_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askdoctor',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=555576, null=True, unique=True),
        ),
    ]
