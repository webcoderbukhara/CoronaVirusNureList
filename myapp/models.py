from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vacsina(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    img = models.ImageField(upload_to='PasportImages/')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    vacsina = models.ForeignKey(Vacsina, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    step1 = models.BooleanField(default=False)
    step2 = models.BooleanField(default=False)
    step3 = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.first_name+self.last_name









