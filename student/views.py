from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import student_tbl

from django.contrib.auth.models import User  # tis id for API
from rest_framework import viewsets  #   this is for the API  
from .serializers import StudentSerializer  # this is for API
#
class Studentviewset(viewsets.ModelViewSet):
    queryset = student_tbl.objects.all()
    serializer_class = StudentSerializer









































# def studentR(request):    

#     return render(request,'studentR.html')

def studentR(request):
    if request.method == 'POST':
        s_name = request.POST['studentName']
        f_name = request.POST['fatherName']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']

        if len(s_name) < 2:
          return HttpResponse("Error")
        else:
           New_student = student_tbl(student_name=s_name,father_name=f_name,age=age,gender=gender,email=email)
           New_student.save()
           return HttpResponse("Success")
    return render(request,'studentR.html')      
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # Save the form data to the database
    #         return redirect('success')  # Redirect to a success page
    # else:
    #     form = StudentForm()

    # return render(request, 'studapp/studentR.html', {'form': form})