from django.db import models
from datetime import date


class Teacher(models.Model):
    """Учитель"""
    fname = models.CharField("Имя", max_length=30)
    mname = models.CharField("Отчество", max_length=30, null=True)
    lname = models.CharField("Фамилия", max_length=40)
    ph_numb = models.CharField("Номер телефона", null=True, unique=True, max_length=40)

    def __str__(self):
        return f'{self.lname} {self.fname} {self.mname}'

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class Student(models.Model):
    """Ученик"""
    fname = models.CharField("Имя", max_length=30)
    mname = models.CharField("Отчество", max_length=30, null=True)
    lname = models.CharField("Фамилия", max_length=40)
    ph_numb = models.CharField("Номер телефона", null=True, unique=True, max_length=40)
    gender = models.CharField("Пол", max_length=7)
    st_class = models.PositiveIntegerField("Класс", default=1)

    def __str__(self):
        return f'{self.lname} {self.fname} - {self.st_class} Класс'

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

class Subject(models.Model):
    """Предмет"""
    name = models.CharField("Название предмета", max_length=30)
    teacher = models.ForeignKey(Teacher, verbose_name="Учитель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} - {self.teacher}'

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Grade(models.Model):
    """Предмет"""
    lesson_topic = models.CharField("Тема урока", max_length=100)
    grade = models.PositiveIntegerField("Оценка", null=True)
    date_gr = models.DateField("Дата выставление оценки", default=date.today)
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.SET_NULL, null=True)
    fgrade = models.PositiveIntegerField("Итоговая оценка", null=True, blank=True)

    def __str__(self):
        return f'{self.subject}  {self.date_gr} {self.grade} {self.student}'

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"



