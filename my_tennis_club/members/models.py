
from django.db import models
class Member(models.Model):
  id=models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  email = models.EmailField(unique=True)
  passwort = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

# Create your models here.
