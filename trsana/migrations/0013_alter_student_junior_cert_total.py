# Generated by Django 4.0.6 on 2022-07-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trsana', '0012_alter_student_rel_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='junior_cert_total',
            field=models.FloatField(verbose_name='مجموع الشهادة الاعدادية'),
        ),
    ]
