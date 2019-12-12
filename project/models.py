from django.db import models
from multiselectfield import MultiSelectField

class Registration(models.Model):
    fn=models.CharField(max_length=100)
    ln=models.CharField(max_length=100)
    un=models.CharField(max_length=100)
    pswd=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)

class Feedback_model(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
   # dat=models.DateTimeField(max_length=50)
    desc=models.CharField(max_length=500,default=False)


class Contact_model(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    courses=(
        ('python','PYTHON'),
         ('java','JAVA'),
          ('.net','.NET')
    )
    courses=MultiSelectField(max_length=100, choices=courses)
    faculty=(
        ('vinod','VINOD'),
        ('sivala','SIVALA'),
        ('kumar','KUMAR')
    )
    faculty=MultiSelectField(max_length=100, choices=faculty)
    gender=models.CharField(max_length=100)





