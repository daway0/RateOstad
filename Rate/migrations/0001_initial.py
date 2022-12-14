# Generated by Django 3.2 on 2022-11-21 21:03

import Rate.helper
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConstValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان مقدار ثابت')),
            ],
            options={
                'verbose_name': 'ConstValue',
                'verbose_name_plural': 'ConstValues',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان درس')),
                ('credits', models.PositiveSmallIntegerField(verbose_name='واحد درس')),
                ('category', models.ForeignKey(blank=True, help_text='پایه، اصلی، تخصصی، تمرکز تخصصی، عمومی، اختیاری', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.constvalue', verbose_name='دسته بندی درس')),
            ],
            options={
                'verbose_name': 'درس',
                'verbose_name_plural': 'درس ها',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_fa', models.CharField(max_length=50, verbose_name='نام')),
                ('last_name_fa', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('first_name_en', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name_en', models.CharField(max_length=50, verbose_name='Last Name')),
                ('is_faculty_member', models.BooleanField(default=False, verbose_name='عضو هیات علمی')),
                ('gender', models.BinaryField(default=0, help_text='عدد 0 نشان دهنده زن و عدد 1 مرد می باشد', verbose_name='جنیست')),
            ],
            options={
                'verbose_name': 'استاد',
                'verbose_name_plural': 'استاد ها',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProfessorLectureSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_students', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='تعداد دانشجویان این درس این ترم این استاد')),
                ('lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.lecture', verbose_name='درس')),
                ('professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.professor', verbose_name='استاد')),
            ],
            options={
                'verbose_name': 'ProfessorLectureSemester',
                'verbose_name_plural': 'ProfessorLectureSemesters',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('code', models.CharField(help_text='مانند: 4011', max_length=5, primary_key=True, serialize=False, verbose_name='کد ترم تحصیلی')),
                ('year', models.PositiveSmallIntegerField(verbose_name='سال تحصیلی')),
                ('is_online', models.BooleanField(default=False, verbose_name='مجازی')),
            ],
            options={
                'verbose_name': 'ترم',
                'verbose_name_plural': 'ترم ها',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('expiration_date', models.DateTimeField(verbose_name=Rate.helper.exp_after_5days)),
                ('related_class', models.ForeignKey(blank=True, help_text='برای هر واحد درسی هر استاد یک نظرسنجی برگزار خواهد شد برای مثال،اگر استاد الف سه کلاس ریاضی 10 نفره داشته باشد، یک صفحه نظرسنجیبا ظرفیت 30 نفر برای اون واحد درسی ساخته خواهد شد', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.professorlecturesemester', verbose_name='کلاس درس')),
            ],
        ),
        migrations.AddField(
            model_name='professorlecturesemester',
            name='semster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.semester', verbose_name='ترم تحصیلی'),
        ),
        migrations.CreateModel(
            name='ProfessorLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.lecture', verbose_name='درس')),
                ('professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.professor', verbose_name='استاد')),
            ],
            options={
                'verbose_name': 'ProfessorLecture',
                'verbose_name_plural': 'ProfessorLectures',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
