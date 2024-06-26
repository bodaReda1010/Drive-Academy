from django.contrib import admin
from . models import Course
# Register your models here.




@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'level' , 'period' , 'created_at' , 'updated_at' , 'is_active']
    
