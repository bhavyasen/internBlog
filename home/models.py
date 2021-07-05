from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    content = models.CharField(max_length=500, default="")
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' + self.name + '' +  self.email
