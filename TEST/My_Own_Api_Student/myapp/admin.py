from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'school', 'join_standard', 'pass_standard', 'favourite_miss', 'pass_or_not',
                    'passby', 'relation_type', 'describe_yourself', 'created_at', 'updated_at']
