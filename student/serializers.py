from rest_framework import serializers
from django.contrib.auth.models import User
from .models import student_tbl

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_tbl
        fields = '__all__'  # Include all fields
        #exclude =['email']
        #read_only_fields = ['id']
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value