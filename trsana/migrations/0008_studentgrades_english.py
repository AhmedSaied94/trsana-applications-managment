# Generated by Django 4.0.6 on 2022-07-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trsana', '0007_studentgrades_spelling'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgrades',
            name='english',
            field=models.IntegerField(default='1', verbose_name='اللغة الانجليزية'),
            preserve_default=False,
        ),
    ]