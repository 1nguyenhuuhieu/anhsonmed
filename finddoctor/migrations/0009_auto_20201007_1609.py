# Generated by Django 3.1.1 on 2020-10-07 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0008_auto_20201007_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='avatar',
            new_name='thumbnail',
        ),
    ]