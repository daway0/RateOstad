from django.db import models

# Create your models here.


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
        to=ConstValue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="دسته بندی درس",
        help_text="پایه، اصلی، تخصصی، تمرکز تخصصی، عمومی، اختیاری",
    )


class ProfessorLecture(models.Model):
    """This is a table that represent the Teachers' lectures"""
    professor = models.ForeignKey(
        to=Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="استاد",
    )
    lecture = models.ForeignKey(
        to=Lecture,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="درس",

    )

class Semester(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ترم'
        verbose_name_plural = 'ترم ها'
    
    code = models.CharField(
        max_length=5,
        verbose_name="کد ترم تحصیلی",
        help_text="مانند: 4011",
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="سال تحصیلی",
    )
    
class ProfessorLectureSemester(models.Model):
    pass


class ConstValue(models.Model):
    """Docstring"""
    title = models.CharField(
        max_length=50,
        verbose_name="عنوان مقدار ثابت",
    )
    parent = models.ForeignKey(
        to=ConstValue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="مقدار ثابت پدر",

    )
