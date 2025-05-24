from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#class Category(models.TextChoices):
   # mobile='mobile'
   # lap_top='lap_top'
   # tools='tools'

#class Product(models.Model):
   # name=models.CharField(max_length=20,blank=False)
   # price=models.DecimalField(decimal_places=2,max_digits=10)
 #   category=models.CharField(max_length=40,choices=Category.choices)
  #  user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
  #  def __str__(self):
   #     return self.name
gender=(
("male","male"),
("female","female"),
("None","None")
)   

major=(
("flutter","flutter"),
("Ui/Ux","Ui/Ux"),
("Graphic_Design","Graphic_Design"),
("Civil_Engineering","Civil_Engineering"),
("Android_Developer","Android_Developer"),
("Django","Django"),
("HR","HR"),
)

class CostumUser(AbstractUser):
    age=models.IntegerField(blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True,default="none")
    gender=models.CharField(max_length=20,choices=gender,default="None",help_text="Gender")
    Your_major_type=models.CharField(max_length=20,choices=major,default="your_major_tupe")

class Post(models.Model):
    inf=models.TextField(max_length=1000,help_text="informations",blank=False,null=False)
    req=models.TextField(max_length=1000,help_text="requirments",blank=False,null=False)
    date=models.DateTimeField(auto_now_add=True,editable=False)
    user=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    email=models.EmailField(blank=False,null=False)
    locations=models.CharField(max_length=70)
    salary=models.DecimalField(decimal_places=2,max_digits=10)
    company_name=models.CharField(max_length=40,blank=False,null=False)
    time_work=models.IntegerField()

class profile(models.Model):
    user=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    major=models.CharField(max_length=50,choices=major)
    Age=models.IntegerField()
    Email=models.EmailField(blank=False,null=False)
    location=models.CharField(max_length=150)
