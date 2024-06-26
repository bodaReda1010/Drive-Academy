from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver



def upload_user_image(instance , file_name):
    extension = file_name.split('.')[1]
    return f'Account/{instance.user}.{extension}'



class Account(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_user_image, height_field=None, width_field=None, max_length=None)
    phone = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)

    def __str__(self):
        return str(self.user)
