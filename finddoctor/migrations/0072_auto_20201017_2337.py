# Generated by Django 3.1.2 on 2020-10-17 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0071_auto_20201017_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='role',
            field=models.CharField(choices=[('BS', 'Bác Sĩ'), ('TK', 'Trưởng Khoa'), ('PK', 'Phó Khoa'), ('DDT', 'Điều dưỡng trưởng')], max_length=200),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=882950, null=True, unique=True),
        ),
    ]
