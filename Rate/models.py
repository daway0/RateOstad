"""Module DOC string"""
from django.db import models


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
        ConstValue,
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
        verbose_name="تعداد دانشجویان این درس در این ترم"
    )
