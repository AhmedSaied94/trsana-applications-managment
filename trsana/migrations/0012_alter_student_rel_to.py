# Generated by Django 4.0.6 on 2022-07-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trsana', '0011_student_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rel_to',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم التابع'),
        ),
    ]
