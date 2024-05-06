from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    Addres=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Course=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name