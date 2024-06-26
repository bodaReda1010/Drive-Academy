from django.contrib import admin
from . models import Comment , Appointment
# Register your models here.



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['account' , 'comment' , 'profession']



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name' , 'course_name' , 'car_type' , 'message']
    
