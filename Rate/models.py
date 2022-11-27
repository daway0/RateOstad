"""Module DOC string"""


from django.db import models
from . import helper


class ConstValue(models.Model):
    """Docstring"""

    # todo آزمایشگاه ها در کدام دسته بندی درسی قرار می گیرند
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

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ConstValue'
        verbose_name_plural = 'ConstValues'

    def __str__(self):
        return self.title


class Professor(models.Model):
    """Docstring"""

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
    gender = models.BooleanField(
        default=0,
        verbose_name="جنیست",
        help_text="عدد 0 نشان دهنده زن و عدد 1 مرد می باشد",
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        gender_prefix = self.gender_prefix_EN
        return f"{gender_prefix} " \
               f"{self.first_name_en.capitalize()} " \
               f"{self.last_name_en.capitalize()}"

    @property
    def fullname_FA(self):
        return f"{self.gender_prefix_FA} " \
               f"{self.first_name_fa} " \
               f"{self.last_name_fa} "

    @property
    def gender_prefix_EN(self):
        if self.gender:
            return "Mr."
        return "Mrs."

    @property
    def gender_prefix_FA(self):
        if self.gender:
            return "آقا"
        return "بانو"


class Lecture(models.Model):
    """Docstring"""
    # todo واحد های عملی و نظری رو باید در درس در نظر بگیرم

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

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lecture'
        verbose_name_plural = 'Lectures'

    def __str__(self):
        return self.title


class ProfessorLecture(models.Model):
    """This is a table that represent the Teachers' lectures"""

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

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProfessorLecture'
        verbose_name_plural = 'ProfessorLectures'

    def __str__(self):
        return f"{self.professor} " \
               f"{self.lecture}"


class Semester(models.Model):
    """DOC STRING"""

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

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    def __str__(self):
        return f"{self.code}"


class Class(models.Model):
    """DOC STRING
        This is also called as the Class
    """

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
    semester = models.ForeignKey(
        Semester,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="ترم تحصیلی"
    )
    number_of_students = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="تعداد دانشجویان",
        help_text="تعداد دانشجویان این درس این ترم این استاد"
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f"{self.lecture} " \
               f"{self.professor.fullname_FA} " \
               f"{self.semester}"


class Survey(models.Model):
    """Docstring"""

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )
    related_class = models.ForeignKey(
        Class,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="کلاس درس",
        help_text="برای هر واحد درسی هر استاد یک نظرسنجی برگزار خواهد شد برای مثال،"
                  "اگر استاد الف سه کلاس ریاضی 10 نفره داشته باشد، یک صفحه نظرسنجی"
                  "با ظرفیت 30 نفر برای اون واحد درسی ساخته خواهد شد",
    )
    expiration_date = models.DateTimeField(
        default=helper.exp_after_5days,
    )
    is_open = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'

    @property
    def number_of_students(self):
        return self.related_class.number_of_students


class Question(models.Model):
    """Docstring"""

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

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class User(models.Model):
    """User model"""
    # شاید نام جدول را به student تغییر دهیم
    # todo this - implement this
    # todo نحوه احراز هویت افراد در کوتاه ترین زمان ممکن، ترجیحا به صورت ناشناس تحقیق شود.
    # راه هایی مثل گرفتن کد ملی، شماره دانشجویی، شماره تلفن همراه اصلا
    # راه های خوبی برای احراز هویت افراد در این اپ نمی باشد

    # todo this - implement this in ConstValue
    type = models.ForeignKey(
        ConstValue,
        on_delete=models.CASCADE,
        verbose_name="",
        help_text="دانشجو، استاد",
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Answer(models.Model):
    """Answer Docstring"""

    # todo

    title = models.CharField(
        max_length=50,
        verbose_name="عنوان جواب",
        help_text="هر جواب ثابتی که بتوان به کمک آن استاد ها را با یکدیگر مقایسه کرد"
                  "برای مثال عنوان جواب می تواند بدین صورت باشد: خنده رو، شوخ طبع، مسط بر درس"
                  "حتی جواب های صفر و یکی مانند بله خیر هم در اینجا قرار خواهد گرفت"
    )
    caption = models.CharField(
        max_length=100,
        verbose_name="توضیحات جواب",
        help_text="کپشن بیشتر برای توضیح عنوان یک جواب در نظر گرفته شده"
                  "برای مثال در سوالی سطح سواد استاد از نظر دانشجو مورد بحث قرار می گیره"
                  "در جواب می توان چند گزینه، مسلط و نامسلط و... را مثال زد"
                  "حال مصادیق نامسلط بودن یک استاد در این فیلد (کپشن) به عنوان"
                  "توضیحات قرار می گیرد و به صورت راهنمای پاسخ در اختیار "
                  "دانشجو قرار می گیرد"
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class QuestionAnswerUser(models.Model):
    """This is the ConstAnswer model"""

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

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'QuestionAnswerUser'
        verbose_name_plural = 'QuestionAnswerUsers'


class Comment(models.Model):
    """برای بیان نظرات شخصی نسبت به استاد از این استفاده می کنیم"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="کاربر",
    )
    text = models.CharField(max_length=400, verbose_name="متن نظر")
    upvote = models.PositiveSmallIntegerField(verbose_name="تعداد موافق ها")
    downvote = models.PositiveSmallIntegerField(verbose_name="تعداد مخالف ها")
    is_visible = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
