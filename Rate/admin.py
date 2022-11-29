from django.contrib import admin
from .models import *


class ConstValueAdmin(admin.ModelAdmin):
    list_display = ("title", "parent")


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("fullname_FA", "__str__")


class LectureAdmin(admin.ModelAdmin):
    list_display = ("title", "credits", "category")


class ProfessorLectureAdmin(admin.ModelAdmin):
    list_display = ("professor", "lecture",
                    "lecture_credits", "lecture_category")

    def lecture_credits(self, obj):
        return obj.lecture.credits

    def lecture_category(self, obj):
        return obj.lecture.category


class SemesterAdmin(admin.ModelAdmin):
    list_display = ["code", "year", "is_online"]


class ClassAdmin(admin.ModelAdmin):
    list_display = ["professor", "lecture",
                    "semester", "class_year", "number_of_students"]

    def class_year(self, obj):
        # todo how to add verbose_name to function like this
        # for more information:
        # this is a function using other tables field and displaying
        # them here
        # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin
        # check the link

        return obj.semester.year


class SurveyAdmin(admin.ModelAdmin):
    list_display = ["related_class",
                    "professor",
                    "lecture",
                    "semester",
                    "creation_date",
                    "expiration_date",
                    "is_open"]
    list_editable = ["is_open"]

    def lecture(self, obj):
        return obj.related_class.lecture

    def professor(self, obj):
        return obj.related_class.professor.fullname_FA

    def semester(self, obj):
        return obj.related_class.semester


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "type"]


class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ["survey", "question", "question_type"]

    def question_type(self, obj):
        return obj.question.type


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "type"]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(ConstValue, ConstValueAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(ProfessorLecture, ProfessorLectureAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Answer, AnswerAdmin)
