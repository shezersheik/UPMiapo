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
    teacher = models.ForeignKey(Teacher, verbose_name="Учитель", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.teacher}'

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Lesson(models.Model):
    """"Урок"""
    subject = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.SET_NULL, null=True, blank=True)
    date_ls = models.DateField("Дата урока", default=date.today)
    lesson_topic = models.CharField("Тема урока", max_length=100)
    homework = models.TextField("Домашнее задание", null=True, blank=True, default='')




    def __str__(self):
        return f'{self.date_ls}  {self.lesson_topic} {self.homework[50:]}...'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

class Grade (models.Model):
    GRADES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    grade = models.CharField("Оценка", max_length=1, choices=GRADES, null=True)
    lesson_topic = models.ForeignKey(Lesson, verbose_name="Тема урока", on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.student}  {self.grade} {self.lesson_topic}'

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

class FinalGrade(models.Model):
    FGRADES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('ЗЧ', 'Зачет'),
        ('НЗ', 'Не зачет')
    )
    fgrade = models.CharField("Оценка", max_length=2, choices=FGRADES, null=True)
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, verbose_name="Предмет", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.subject}, {self.student} {self.fgrade}'

    class Meta:
        verbose_name = "Итоговая оценка"
        verbose_name_plural = "Итоговые оценки"