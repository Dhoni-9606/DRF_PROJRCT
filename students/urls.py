from django.urls import path
from .import views

urlpatterns=[
    path('students/',views.student_api),
    path('courses/',views.courses_api),
    path('trainers/',views.trainers_api),
    path('students/<int:id>/',views.student_details_api),
]