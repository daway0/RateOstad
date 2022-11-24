# Generated by Django 3.2 on 2022-11-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rate', '0004_alter_professor_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'managed': True, 'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': True, 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='lecture',
            options={'managed': True, 'verbose_name': 'Lecture', 'verbose_name_plural': 'Lectures'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'managed': True, 'verbose_name': 'Professor', 'verbose_name_plural': 'Professors'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'managed': True, 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='questionansweruser',
            options={'managed': True, 'verbose_name': 'QuestionAnswerUser', 'verbose_name_plural': 'QuestionAnswerUsers'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'managed': True, 'verbose_name': 'Semester', 'verbose_name_plural': 'Semesters'},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'managed': True, 'verbose_name': 'Survey', 'verbose_name_plural': 'Surveys'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='survey',
            name='is_open',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='professorlecturesemester',
            name='number_of_students',
            field=models.PositiveSmallIntegerField(blank=True, help_text='تعداد دانشجویان این درس این ترم این استاد', null=True, verbose_name='تعداد دانشجویان'),
        ),
        migrations.AlterModelTable(
            name='answer',
            table='',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='',
        ),
        migrations.AlterModelTable(
            name='question',
            table='',
        ),
        migrations.AlterModelTable(
            name='questionansweruser',
            table='',
        ),
        migrations.AlterModelTable(
            name='survey',
            table='',
        ),
        migrations.AlterModelTable(
            name='user',
            table='',
        ),
    ]
