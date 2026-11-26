from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers
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

# @api_view(['GET'])
# def student_api(request):

#     return Response(students)

@api_view(['GET', 'POST'])
def student_api(request):

    # GET: Retrieve students
    if request.method == 'GET':

        name = request.query_params.get('name')

        if name:
            filtered_students = []

            for student in students:
                if student['name'].lower() == name.lower():
                    filtered_students.append(student)

            return Response(
                filtered_students,
                status=status.HTTP_200_OK
            )

        return Response(
            students,
            status=status.HTTP_200_OK
        )

    # POST: Create a student
    elif request.method == 'POST':

        name = request.data.get('name')
        course = request.data.get('course')

        if not name or not course:
            return Response(
                {"error": "Name and course are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        new_student = {
            "id": len(students) + 1,
            "name": name,
            "course": course
        }

        students.append(new_student)

        return Response(
            new_student,
            status=status.HTTP_201_CREATED
        )

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

@api_view(['GET'])
def student_seria_api(request):

    students = Student.objects.all()

    serializer = StudentSerializers(students, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer=StudentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data)