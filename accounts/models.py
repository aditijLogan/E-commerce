from django.db import models
from django.contrib.auth.models import User
#django user model override
from base.models import BaseModel
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")#by this we will connect profile
    is_mail_verified = models.BooleanField(default=False)
    email_tokaen = models.CharField(max_length=100, null=True,blank=True)
    profile_image = models.ImageField(upload_to="profile")     



@receiver(post_save , sender = User) #making the signal
def  send_email_token(sender , instance , created , **kwargs): #kwargs= dict that holds parameters and can be used by passing through a function
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)#saving the user
            email = instance.email
            send_account_activation_email(email , email_token)#created a function and this function we write in base 

    except Exception as e:
        print(e)