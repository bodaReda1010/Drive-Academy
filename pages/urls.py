from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [

    path('write_comment/',views.write_comment,name='write_comment'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('features/',views.features,name='features'),
    path('appointment/',views.appointment,name='appointment'),
    
]
