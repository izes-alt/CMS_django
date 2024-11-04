from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    
   # path('',views.studentM, name='student'),
    path('',views.studentR, name='studentR'),
   # path('success/', TemplateView.as_view(template_name="studapp/success.html"))

   
]
