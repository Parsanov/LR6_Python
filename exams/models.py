from django.db import models


class Subject(models.Model):
    """
    Навчальний предмет.
    name: CharField(100) — назва, до 100 символів
    semester: PositiveSmallIntegerField — семестр 1-12
    credits: PositiveSmallIntegerField — кредити ECTS 1-10
    """
    name     = models.CharField(max_length=100, verbose_name="Назва предмета")
    semester = models.PositiveSmallIntegerField(verbose_name="Семестр")
    credits  = models.PositiveSmallIntegerField(verbose_name="Кредити")

    class Meta:
        verbose_name        = "Предмет"
        verbose_name_plural = "Предмети"
        ordering            = ["name"]

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    Студент.
    first_name/last_name: CharField(50) — до 50 символів
    birth_date: DateField — дата народження
    gender: CharField(1) — 'M'/'F'
    """
    GENDER_CHOICES = [("M", "Чоловік"), ("F", "Жінка")]

    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name  = models.CharField(max_length=50, verbose_name="Прізвище")
    birth_date = models.DateField(verbose_name="Дата народження")
    gender     = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Стать")

    class Meta:
        verbose_name        = "Студент"
        verbose_name_plural = "Студенти"
        ordering            = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Exam(models.Model):
    """
    Іспит (дочірня таблиця).
    subject: ForeignKey → Subject CASCADE
    student: ForeignKey → Student CASCADE
    date: DateField — дата іспиту
    mark: PositiveSmallIntegerField — оцінка 0-100
    """
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        verbose_name="Предмет", related_name="exams"
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        verbose_name="Студент", related_name="exams"
    )
    date = models.DateField(verbose_name="Дата іспиту")
    mark = models.PositiveSmallIntegerField(verbose_name="Оцінка")

    class Meta:
        verbose_name        = "Іспит"
        verbose_name_plural = "Іспити"
        ordering            = ["-date"]

    def __str__(self):
        return f"{self.student} — {self.subject} ({self.date}): {self.mark}"
