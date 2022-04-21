from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View

from .models import Grade, Student, Subject


class Login(View):
    """Список оценок"""
    def get(self, request):
        grades = Grade.objects.all()
        subject = Subject.objects.all()

        return render(request, "auth.html", {"grades_list": grades, "subjects_list": subject})


class GradesViewStudent(View):
    """Список оценок ученика"""

    def get(self, request, pk):
        grades = Grade.objects.all()
        student = Student.objects.get(id=pk)
        for i in grades:
            if i.student.id == student.id:
                grades = Grade.objects.filter(student=student.id)
        return render(request, "grades.html", {"grades_list": grades})