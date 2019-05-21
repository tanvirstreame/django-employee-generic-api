from django.contrib import admin
from django.urls import path, include
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('employee.urls'),name="employee"), 
]
