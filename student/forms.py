from django import forms
from .models import student_tbl

class StudentForm(forms.ModelForm):
    class Meta:
        model = student_tbl
        fields = ['student_name', 'father_name', 'age', 'gender', 'email']