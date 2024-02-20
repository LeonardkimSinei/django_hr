from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.employee_form),
    path('employee/',include('employee_register.urls') ),
]
