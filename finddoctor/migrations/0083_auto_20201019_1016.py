# Generated by Django 3.1.1 on 2020-10-19 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finddoctor', '0082_auto_20201019_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='doctor',
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=945195, null=True, unique=True),
        ),
    ]
