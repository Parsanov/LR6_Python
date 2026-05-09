from django.contrib import admin
from .models import Subject, Student, Exam


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display  = ("name", "semester", "credits")
    search_fields = ("name",)
    list_filter   = ("semester",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ("last_name", "first_name", "birth_date", "gender")
    search_fields = ("last_name", "first_name")
    list_filter   = ("gender",)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display   = ("student", "subject", "date", "mark")
    list_filter    = ("subject", "date")
    search_fields  = ("student__last_name", "subject__name")
    date_hierarchy = "date"
