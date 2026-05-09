from django import forms
from .models import Exam, Subject


class ExamForm(forms.ModelForm):
    """Форма додавання іспиту на основі моделі."""
    class Meta:
        model  = Exam
        fields = ["subject", "student", "date", "mark"]
        widgets = {
            "subject": forms.Select(attrs={"class": "form-select"}),
            "student": forms.Select(attrs={"class": "form-select"}),
            "date":    forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "mark":    forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 100}),
        }


class Query1Form(forms.Form):
    """Запит 1 — вибір предмета через select."""
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        label="Предмет",
        widget=forms.Select(attrs={"class": "form-select"}),
    )


class Query2Form(forms.Form):
    """Запит 2 — вибір предмета та дати іспиту."""
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        label="Предмет",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    date = forms.DateField(
        label="Дата іспиту",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )


class Query5Form(forms.Form):
    """Запит 5 — пошук студентів нижче середньої."""
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        label="Предмет (або залиште порожнім для всіх)",
        required=False,
        empty_label="— Всі предмети —",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
