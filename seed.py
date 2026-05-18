from exams.models import Subject, Student, Exam
from datetime import date

# Предмети
s1 = Subject.objects.create(name='Математичний аналіз', semester=1, credits=5)
s2 = Subject.objects.create(name='Фізика', semester=2, credits=4)
s3 = Subject.objects.create(name='Програмування', semester=1, credits=6)
s4 = Subject.objects.create(name='Бази даних', semester=3, credits=4)
s5 = Subject.objects.create(name='Алгоритми та структури даних', semester=2, credits=5)

# Студенти
st1  = Student.objects.create(first_name='Іван',    last_name='Петренко',   birth_date=date(2003,5,12),  gender='M')
st2  = Student.objects.create(first_name='Олена',   last_name='Коваль',     birth_date=date(2004,3,7),   gender='F')
st3  = Student.objects.create(first_name='Олексій', last_name='Шевченко',   birth_date=date(2003,8,22),  gender='M')
st4  = Student.objects.create(first_name='Марія',   last_name='Бондаренко', birth_date=date(2004,1,15),  gender='F')
st5  = Student.objects.create(first_name='Дмитро',  last_name='Мельник',    birth_date=date(2003,11,3),  gender='M')
st6  = Student.objects.create(first_name='Анна',    last_name='Кравченко',  birth_date=date(2004,6,28),  gender='F')
st7  = Student.objects.create(first_name='Сергій',  last_name='Лисенко',    birth_date=date(2002,4,10),  gender='M')
st8  = Student.objects.create(first_name='Наталія', last_name='Гончаренко', birth_date=date(2003,9,17),  gender='F')
st9  = Student.objects.create(first_name='Андрій',  last_name='Тимченко',   birth_date=date(2004,2,5),   gender='M')
st10 = Student.objects.create(first_name='Юлія',    last_name='Павленко',   birth_date=date(2003,7,19),  gender='F')

# Іспити
Exam.objects.create(subject=s1, student=st1,  date=date(2025,1,15), mark=87)
Exam.objects.create(subject=s1, student=st3,  date=date(2025,1,15), mark=74)
Exam.objects.create(subject=s1, student=st4,  date=date(2025,1,15), mark=91)
Exam.objects.create(subject=s1, student=st5,  date=date(2025,1,15), mark=58)
Exam.objects.create(subject=s1, student=st6,  date=date(2025,1,15), mark=82)
Exam.objects.create(subject=s2, student=st2,  date=date(2025,1,20), mark=72)
Exam.objects.create(subject=s2, student=st3,  date=date(2025,1,20), mark=65)
Exam.objects.create(subject=s2, student=st9,  date=date(2025,1,20), mark=88)
Exam.objects.create(subject=s2, student=st10, date=date(2025,1,20), mark=45)
Exam.objects.create(subject=s3, student=st1,  date=date(2025,2,5),  mark=93)
Exam.objects.create(subject=s3, student=st4,  date=date(2025,2,5),  mark=61)
Exam.objects.create(subject=s3, student=st5,  date=date(2025,2,5),  mark=77)
Exam.objects.create(subject=s4, student=st2,  date=date(2025,2,10), mark=84)
Exam.objects.create(subject=s4, student=st6,  date=date(2025,2,10), mark=55)
Exam.objects.create(subject=s4, student=st9,  date=date(2025,2,10), mark=90)
Exam.objects.create(subject=s5, student=st1,  date=date(2025,2,20), mark=70)
Exam.objects.create(subject=s5, student=st3,  date=date(2025,2,20), mark=68)
Exam.objects.create(subject=s5, student=st10, date=date(2025,2,20), mark=52)

print('Предметів:', Subject.objects.count())
print('Студентів:', Student.objects.count())
print('Іспитів:',   Exam.objects.count())
