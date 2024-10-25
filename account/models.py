from django.db import models
from django.contrib.auth.models import User


class Profile_Model(models.Model):
 
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    is_vendor=models.BooleanField(default=False)

    def __str__(self): return self.user.username 

