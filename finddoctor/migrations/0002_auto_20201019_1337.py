# Generated by Django 3.1.1 on 2020-10-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=829580, null=True, unique=True),
        ),
    ]
