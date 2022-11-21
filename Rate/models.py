"""Module DOC string"""

import datetime
from django.db import models

import Rate
from . import helper


class ConstValue(models.Model):
    """Docstring"""

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ConstValue'
        verbose_name_plural = 'ConstValues'

    title = models.CharField(
        max_length=50,
        verbose_name="عنوان مقدار ثابت",
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="مقدار ثابت پدر",
    )


class Professor(models.Model):
    """Docstring"""

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'استاد'
        verbose_name_plural = 'استاد ها'

    first_name_fa = models.CharField(
        max_length=50,
        verbose_name="نام",
    )
    last_name_fa = models.CharField(
        max_length=50,
        verbose_name="نام خانوادگی",
    )
    first_name_en = models.CharField(
        max_length=50,
        verbose_name="First Name",
    )
    last_name_en = models.CharField(
        max_length=50,
        verbose_name="Last Name",
    )
    is_faculty_member = models.BooleanField(
        default=False,
        verbose_name="عضو هیات علمی",
    )
    gender = models.BinaryField(
        default=0,
        verbose_name="جنیست",
        help_text="عدد 0 نشان دهنده زن و عدد 1 مرد می باشد",
    )


class Lecture(models.Model):
    """Docstring"""

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'درس'
        verbose_name_plural = 'درس ها'

    title = models.CharField(
        max_length=50,
        verbose_name="عنوان درس",
    )
    credits = models.PositiveSmallIntegerField(
        verbose_name="واحد درس",
    )
    category = models.ForeignKey(
        ConstValue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="دسته بندی درس",
        help_text="پایه، اصلی، تخصصی، تمرکز تخصصی، عمومی، اختیاری",
    )


class ProfessorLecture(models.Model):
    """This is a table that represent the Teachers' lectures"""

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProfessorLecture'
        verbose_name_plural = 'ProfessorLectures'

    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="استاد",
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="درس",
    )


class Semester(models.Model):
    """DOC STRING"""

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ترم'
        verbose_name_plural = 'ترم ها'

    code = models.CharField(
        primary_key=True,
        max_length=5,
        verbose_name="کد ترم تحصیلی",
        help_text="مانند: 4011",
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="سال تحصیلی",
    )
    is_online = models.BooleanField(
        default=False,
        verbose_name="مجازی",
    )


class ProfessorLectureSemester(models.Model):
    """DOC STRING"""

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProfessorLectureSemester'
        verbose_name_plural = 'ProfessorLectureSemesters'

    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="استاد",
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="درس",
    )
    semster = models.ForeignKey(
        Semester,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="ترم تحصیلی"
    )
    number_of_students = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="تعداد دانشجویان این درس این ترم این استاد"
    )


class Survey(models.Model):
    """Docstring"""

    class Meta:
        pass

    create_date = models.DateTimeField(
        datetime.datetime.now,
    )
    related_class = models.ForeignKey(
        ProfessorLectureSemester,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="کلاس درس",
        help_text="برای هر واحد درسی هر استاد یک نظرسنجی برگزار خواهد شد برای مثال،" \
                  "اگر استاد الف سه کلاس ریاضی 10 نفره داشته باشد، یک صفحه نظرسنجی" \
                  "با ظرفیت 30 نفر برای اون واحد درسی ساخته خواهد شد",
    )
    expiration_date = models.DateTimeField(
        default=helper.exp_after_5days,
    )

    @property
    def number_of_students(self):
        return self.related_class.number_of_students


class Question(models.Model):
    """Docstring"""

    class Meta:
        pass

    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        verbose_name=""
    )
    question = models.CharField(
        max_length=150,
    )
    note = models.CharField(
        max_length=400,
        null=True,
        blank=True,
    )
    display_order = models.PositiveSmallIntegerField(
        verbose_name="",

    )
    # todo this - implement this in ConstValue
    type = models.ForeignKey(
        ConstValue,
        on_delete=models.CASCADE,
        verbose_name="",
        help_text="اینکه رادیو باتن باشه، یا چند گزینه ای یا بله و خیر و...",
    )


class User(models.Model):
    """User model"""

    # todo this - implement this
    class Meta:
        pass

    # todo this - implement this in ConstValue
    type = models.ForeignKey(
        ConstValue,
        on_delete=models.CASCADE,
        verbose_name="",
        help_text="دانشجو، استاد",
    )


class QuestionAnswerUser(models.Model):
    """This is the ConstAnswer model"""

    class Meta:
        pass

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="",
    )
    answer = models.ForeignKey(
        ConstValue,
        on_delete=models.CASCADE,
        verbose_name="",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="",
    )


class Comment(models.Model):
    """برای بیان نظرات شخصی نسبت به استاد از این استفاده می کنیم"""
    pass
