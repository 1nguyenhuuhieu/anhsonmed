# Generated by Django 3.1.2 on 2020-10-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0073_auto_20201017_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookapartment',
            name='isdone',
            field=models.CharField(blank=True, default='Đang chờ khám', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=271410, null=True, unique=True),
        ),
    ]
