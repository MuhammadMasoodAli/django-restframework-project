from dataclasses import fields
from .models import Student, Course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course,
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # Custom validation
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError('Cannot enroll into this course. Student must be 18 years old.')
        return value


