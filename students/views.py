from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
students = [
        {
            "id": 1,
            "name": "Rahul",
            "course": "Python"
        },
        {
            "id": 2,
            "name": "Kiran",
            "course": "Django"
        },
        {
            "id": 3,
            "name": "Arun",
            "course": "Java"
        }
    ]

@api_view(['GET'])
def student_api(request):

    return Response(students)

@api_view(['GET'])
def courses_api(reauest):
    courses_list=[
        {
            "course1":"python",
            "course2":"DRF",
            "course3":"java",
                        

        }
    ]
    return Response(courses_list)

@api_view(['GET'])
def trainers_api(request):
    trainers_list=[
         {
      "id": 101,
      "name": "John Smith",
      "experience": 5
    },
    {
      "id": 102,
      "name": "Sarah Johnson",
      "experience": 8
    },
    {
      "id": 103,
      "name": "Michael Brown",
      "experience": 3
    },
    {
      "id": 104,
      "name": "Emily Davis",
      "experience": 10
    },
    {
      "id": 105,
      "name": "David Wilson",
      "experience": 6
    }
    ]
    return Response(trainers_list)


@api_view(['GET'])
def student_details_api(request,id):

    for student in students:
        if student["id"]==id:
            return Response(student)
    return Response(
        {
            "message":"student not found"
        },
        status=status.HTTP_404_NOT_FOUND
    )