from rest_framework import viewsets

from .models import *
from .serializers import *


class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class InstructorViewSet(viewsets.ModelViewSet):
  queryset = Instructor.objects.all()
  serializer_class = InstructorSerializer


class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer


class GradeViewSet(viewsets.ModelViewSet):
  queryset = Grade.objects.all()
  serializer_class = GradeSerializer

  class Meta:
    model = Grade
    fields = ['id', 'score', 'course', 'student']

    def get_letter_grade(self, obj):
      if obj.score >= 90:
        return "A"
      if obj.score >= 80:
        return "B"
      if obj.score >= 70:
        return "C"
      if obj.score >= 60:
        return "D"
      else: return "F"
