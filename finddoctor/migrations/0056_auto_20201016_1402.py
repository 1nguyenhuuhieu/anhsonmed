# Generated by Django 3.1.1 on 2020-10-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0055_auto_20201016_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=688396, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bookapartment',
            name='status',
            field=models.CharField(blank=True, choices=[('ĐC', 'Đang Chờ Xác Nhận'), ('ĐX', 'Đã Khám Xong')], default='Đang Chờ Xác Nhận', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookapartment',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=483091, null=True),
        ),
    ]