# Generated by Django 3.1.1 on 2020-10-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0013_auto_20201020_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=216338, null=True, unique=True),
        ),
    ]