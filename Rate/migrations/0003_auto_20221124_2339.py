# Generated by Django 3.2 on 2022-11-24 20:09

import Rate.helper
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rate', '0002_constvalue_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='هر جواب ثابتی که بتوان به کمک آن استاد ها را با یکدیگر مقایسه کردبرای مثال عنوان جواب می تواند بدین صورت باشد: خنده رو، شوخ طبع، مسط بر درسحتی جواب های صفر و یکی مانند بله خیر هم در اینجا قرار خواهد گرفت', max_length=50, verbose_name='عنوان جواب')),
                ('caption', models.CharField(help_text='کپشن بیشتر برای توضیح عنوان یک جواب در نظر گرفته شدهبرای مثال در سوالی سطح سواد استاد از نظر دانشجو مورد بحث قرار می گیرهدر جواب می توان چند گزینه، مسلط و نامسلط و... را مثال زدحال مصادیق نامسلط بودن یک استاد در این فیلد (کپشن) به عنوانتوضیحات قرار می گیرد و به صورت راهنمای پاسخ در اختیار دانشجو قرار می گیرد', max_length=100, verbose_name='توضیحات جواب')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('note', models.CharField(blank=True, max_length=400, null=True)),
                ('display_order', models.PositiveSmallIntegerField(verbose_name='')),
            ],
        ),
        migrations.RenameField(
            model_name='professorlecturesemester',
            old_name='semster',
            new_name='semester',
        ),
        migrations.AlterField(
            model_name='survey',
            name='expiration_date',
            field=models.DateTimeField(default=Rate.helper.exp_after_5days),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(help_text='دانشجو، استاد', on_delete=django.db.models.deletion.CASCADE, to='Rate.constvalue', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rate.constvalue', verbose_name='')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rate.question', verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rate.user', verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rate.survey', verbose_name=''),
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ForeignKey(help_text='اینکه رادیو باتن باشه، یا چند گزینه ای یا بله و خیر و...', on_delete=django.db.models.deletion.CASCADE, to='Rate.constvalue', verbose_name=''),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400, verbose_name='متن نظر')),
                ('upvote', models.PositiveSmallIntegerField(verbose_name='تعداد موافق ها')),
                ('downvote', models.PositiveSmallIntegerField(verbose_name='تعداد مخالف ها')),
                ('is_visible', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rate.user', verbose_name='کاربر')),
            ],
        ),
    ]
