from django.db import models

class Registration(models.Model):
    fn=models.CharField(max_length=100)
    ln=models.CharField(max_length=100)
    un=models.CharField(max_length=100)
    pswd=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    image=models.FileField(upload_to='vinod',default=False)

class Feedback_model(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
   # dat=models.DateTimeField(max_length=50)
    desc=models.CharField(max_length=500,default=False)







