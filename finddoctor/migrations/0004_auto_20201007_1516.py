# Generated by Django 3.1.1 on 2020-10-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0003_reward_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.TextField(),
        ),
    ]