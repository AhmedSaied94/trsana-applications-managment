# Generated by Django 4.0.6 on 2022-07-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trsana', '0005_alter_student_guardian_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rel',
            field=models.BooleanField(default=False, verbose_name='تابع'),
        ),
        migrations.AddField(
            model_name='student',
            name='rel_to',
            field=models.CharField(default='ahmed', max_length=50, verbose_name='اسم التابع'),
            preserve_default=False,
        ),
    ]
