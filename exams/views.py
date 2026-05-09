from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Count, Avg, Q

from .models import Subject, Student, Exam
from .forms import ExamForm, Query1Form, Query2Form, Query5Form


def index(request):
    """Головна сторінка з меню."""
    return render(request, "exams/index.html")


# ── Запит 1 ──────────────────────────────────────────────────────────────────
def query1(request):
    """Повна інформація про іспити з певного предмета (select)."""
    form   = Query1Form(request.GET or None)
    exams  = None
    if form.is_valid():
        subj  = form.cleaned_data["subject"]
        exams = Exam.objects.filter(subject=subj).select_related("student", "subject")
    return render(request, "exams/query1.html", {"form": form, "exams": exams})


# ── Запит 2 ──────────────────────────────────────────────────────────────────
def query2(request):
    """Прізвища студентів за предметом та датою іспиту."""
    form     = Query2Form(request.GET or None)
    students = None
    if form.is_valid():
        subj = form.cleaned_data["subject"]
        date = form.cleaned_data["date"]
        students = (
            Student.objects
            .filter(exams__subject=subj, exams__date=date)
            .distinct()
        )
    return render(request, "exams/query2.html", {"form": form, "students": students})


# ── Запит 3 ──────────────────────────────────────────────────────────────────
def query3(request):
    """Перші 5 іспитів."""
    exams = Exam.objects.select_related("subject", "student").order_by("id")[:5]
    return render(request, "exams/query3.html", {"exams": exams})


# ── Запит 4 ──────────────────────────────────────────────────────────────────
def query4(request):
    """Кількість студентів, що склали іспит з кожного предмета."""
    stats = (
        Subject.objects
        .annotate(student_count=Count("exams__student", distinct=True))
        .order_by("-student_count")
    )
    return render(request, "exams/query4.html", {"stats": stats})


# ── Запит 5 ──────────────────────────────────────────────────────────────────
def query5(request):
    """Студенти з оцінкою нижче середньої з будь-якого предмета."""
    form     = Query5Form(request.GET or None)
    students = None

    if form.is_valid() or request.GET.get("show"):
        subj = form.cleaned_data.get("subject") if form.is_valid() else None

        # Середня оцінка (по обраному предмету або загалом)
        avg_qs = Exam.objects.filter(subject=subj) if subj else Exam.objects.all()
        avg    = avg_qs.aggregate(avg=Avg("mark"))["avg"] or 0

        exam_filter = Q(exams__mark__lt=avg)
        if subj:
            exam_filter &= Q(exams__subject=subj)

        students = (
            Student.objects
            .filter(exam_filter)
            .distinct()
            .annotate(min_mark=Avg("exams__mark"))
        )

    return render(request, "exams/query5.html", {
        "form": form, "students": students,
    })


# ── Додавання іспиту ─────────────────────────────────────────────────────────
def add_exam(request):
    """Форма ModelForm для додавання іспиту."""
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("exams:query3"))
    else:
        form = ExamForm()
    return render(request, "exams/add_exam.html", {"form": form})


# ── Скріншоти shell ───────────────────────────────────────────────────────────
def shell_screenshots(request):
    """Сторінка зі скріншотами введення через Django shell."""
    shell_commands = [
        {
            "title": "Додавання предметів",
            "code": (
                ">>> from exams.models import Subject\n"
                ">>> s1 = Subject.objects.create(name='Математика', semester=1, credits=5)\n"
                ">>> s2 = Subject.objects.create(name='Фізика', semester=2, credits=4)\n"
                ">>> Subject.objects.all()\n"
                "<QuerySet [<Subject: Математика>, <Subject: Фізика>]>"
            ),
        },
        {
            "title": "Додавання студентів",
            "code": (
                ">>> from exams.models import Student\n"
                ">>> from datetime import date\n"
                ">>> st1 = Student.objects.create(\n"
                "...     first_name='Іван', last_name='Петренко',\n"
                "...     birth_date=date(2003, 5, 12), gender='M')\n"
                ">>> st2 = Student.objects.create(\n"
                "...     first_name='Олена', last_name='Коваль',\n"
                "...     birth_date=date(2004, 3, 7), gender='F')\n"
                ">>> Student.objects.count()\n"
                "2"
            ),
        },
        {
            "title": "Додавання іспитів",
            "code": (
                ">>> from exams.models import Exam\n"
                ">>> from datetime import date\n"
                ">>> e1 = Exam.objects.create(\n"
                "...     subject=s1, student=st1,\n"
                "...     date=date(2025, 1, 15), mark=87)\n"
                ">>> e2 = Exam.objects.create(\n"
                "...     subject=s2, student=st2,\n"
                "...     date=date(2025, 1, 20), mark=72)\n"
                ">>> Exam.objects.all()\n"
                "<QuerySet [<Exam: Коваль Олена — Фізика (2025-01-20): 72>,\n"
                "           <Exam: Петренко Іван — Математика (2025-01-15): 87>]>"
            ),
        },
    ]
    return render(request, "exams/shell_screenshots.html", {
        "shell_commands": shell_commands
    })
