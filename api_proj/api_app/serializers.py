from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'age', 'courses']


class InstructorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Instructor
    fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['id', 'name', 'instructor']


class GradeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grade
    fields = ['id', 'score', 'course', 'student']

#     def get_letter_grade(self, obj):
#       if obj.score >= 90:
#         return "A"
#       if obj.score >= 80:
#         return "B"
#       if obj.score >= 70:
#         return "C"
#       if obj.score >= 60:
#         return "D"
#       else: return "F"
      