# Generated by Django 4.0.6 on 2022-07-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_account', '0003_alter_userprofile_gender_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
