from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.



def upload_course_image(instance , file_name):
    extension = file_name.split('.')[1]
    return f'Course/{instance.name}.{extension}'


LEVEL = (
    ('Beginner','Beginner'),
    ('Mid-Level','Mid-Level'),
    ('Expert','Expert'),
)


class Course(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True , null=True , blank=True)
    image = models.ImageField(upload_to=upload_course_image, height_field=None, width_field=None, max_length=None)
    price = models.FloatField(default = 0)
    description = models.TextField()
    level = models.CharField(max_length=100,choices=LEVEL)
    period = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = True)

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course , self).save(*args, **kwargs)


    def __str__(self):
        return self.name
