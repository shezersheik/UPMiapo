from django.urls import path
from . import views

urlpatterns = [
    path("", views.Login.as_view()),
    path("<int:pk>/", views.GradesViewStudent.as_view())
]