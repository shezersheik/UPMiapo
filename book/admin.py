from django.contrib import admin

from . models import Student, Teacher, Subject, Grade,Lesson,FinalGrade

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Lesson)
admin.site.register(FinalGrade)

