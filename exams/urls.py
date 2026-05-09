from django.urls import path
from . import views

app_name = "exams"

urlpatterns = [
    path("",              views.index,             name="index"),
    path("query1/",       views.query1,             name="query1"),
    path("query2/",       views.query2,             name="query2"),
    path("query3/",       views.query3,             name="query3"),
    path("query4/",       views.query4,             name="query4"),
    path("query5/",       views.query5,             name="query5"),
    path("add-exam/",     views.add_exam,           name="add_exam"),
    path("shell/",        views.shell_screenshots,  name="shell"),
]
