from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets
from .task import send_course_email

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def signUp_to_course(self, request):
        query = request.query_params.get('course_id')
        id = request.GET.get('student_id')
        if not query or not id:
            return Response({'message': 'Ошибка!'}, status=status.HTTP_404_NOT_FOUND)
        course = Courses.objects.get(pk=query)
        student = Student.objects.get(pk=id)
        student.student_courses.add(course)
        send_course_email.delay(student.first_name,course.name, student.email, course.start_date)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer

# Create your views here.
