from django.contrib import admin
from django.urls import path, include
from.views import *
urlpatterns = [
    path('students', StudentCurd.as_view(), name="students_list_or_create"),
    path('students/<int:pk>/', StudentCurdd.as_view(), name="students_get_or_update"),
]