from django.contrib import admin
from .models import *

@admin.register(Courses)
class CourserAdmin(admin.ModelAdmin):
    list_display = ['name', 'ruler', 'duration']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ['course', 'day', 'time_duration']

# Register your models here.
