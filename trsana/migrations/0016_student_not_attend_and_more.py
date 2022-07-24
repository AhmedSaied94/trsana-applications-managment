# Generated by Django 4.0.6 on 2022-07-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trsana', '0015_alter_student_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='not_attend',
            field=models.BooleanField(default=False, verbose_name='لم يحضر'),
        ),
        migrations.AlterField(
            model_name='committeeevaluation',
            name='committee_chairman',
            field=models.FloatField(verbose_name='رئيس اللجنة'),
        ),
        migrations.AlterField(
            model_name='committeeevaluation',
            name='first_member',
            field=models.FloatField(verbose_name='العضو الاول'),
        ),
        migrations.AlterField(
            model_name='committeeevaluation',
            name='forth_member',
            field=models.FloatField(verbose_name='العضو الرابع'),
        ),
        migrations.AlterField(
            model_name='committeeevaluation',
            name='second_member',
            field=models.FloatField(verbose_name='العضو الثاني'),
        ),
        migrations.AlterField(
            model_name='committeeevaluation',
            name='third_member',
            field=models.FloatField(verbose_name='العضو الثالث'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='arabic',
            field=models.FloatField(verbose_name='اللغة العربية'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='computer',
            field=models.FloatField(verbose_name='الحاسب الالي'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='english',
            field=models.FloatField(verbose_name='اللغة الانجليزية'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='math',
            field=models.FloatField(verbose_name='الرياضيات'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='science',
            field=models.FloatField(verbose_name='العلوم'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='social_studies',
            field=models.FloatField(verbose_name='الدراسات الاجتماعية'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='spelling',
            field=models.FloatField(verbose_name='املاء'),
        ),
    ]