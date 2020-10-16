# Generated by Django 3.1.1 on 2020-10-16 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0059_auto_20201016_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finddoctor.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='vertify_code',
            field=models.IntegerField(blank=True, default=914783, null=True, unique=True),
        ),
    ]
