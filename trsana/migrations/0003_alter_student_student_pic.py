# Generated by Django 4.0.5 on 2022-07-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trsana', '0002_alter_student_junior_cert_year_studentgrades_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_pic',
            field=models.ImageField(upload_to='students', verbose_name='صورة الطالب'),
        ),
    ]
