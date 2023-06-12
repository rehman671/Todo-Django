from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomUser(User):
    Uid = models.AutoField(primary_key= True)
    def __str__(self):
        return self.username
    



class Task(models.Model):
    Tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    desc = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' '+ self.user.username
    
