# Generated by Django 3.1.2 on 2020-10-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0026_auto_20201021_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=659311, null=True, unique=True),
        ),
    ]
