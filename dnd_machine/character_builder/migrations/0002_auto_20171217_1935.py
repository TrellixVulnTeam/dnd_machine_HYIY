# Generated by Django 2.0 on 2017-12-18 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='character',
        ),
        migrations.AddField(
            model_name='language',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='character_builder.Race'),
        ),
        migrations.AlterField(
            model_name='racetrait',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='race_traits', to='character_builder.Race'),
        ),
    ]
