# Generated by Django 2.0 on 2018-01-05 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0012_auto_20180105_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savingthrow',
            old_name='character_name',
            new_name='character',
        ),
    ]