from django.shortcuts import render,HttpResponse
from .models import Registration,Feedback_model
from .forms import Registration_form,Login_form,Feedback_from



def login(request):

    if request.method=="POST":
        rform = Login_form(request.POST)
        if rform.is_valid():
            use=request.POST.get('uname')
            ps=request.POST.get("passw")
            user1=Registration.objects.filter(un=use)
            paswd1=Registration.objects.filter(pswd=ps)
            if user1 and paswd1:
                return render(request,"home.html")
            else:
                return HttpResponse("fail")
        else:
            return HttpResponse("invalid data")

    else:
        rform=Login_form()
        return render(request,"login.html",{"rform":rform})


def reg(request):
    if request.method=="POST":
        rform=Registration_form(request.POST)
        if rform.is_valid():
            fname=request.POST.get("fname")
            lname=request.POST.get("ln")
            un=request.POST.get("un")
            pswd=request.POST.get("pswd")
            mobile=request.POST.get("mobile")
            email=request.POST.get("email")
            photo=request.POST.get("image")
            Registration(fn=fname,ln=lname,un=un,pswd=pswd,mobile=mobile,email=email,image=photo).save()
            rform=Registration_form()
            return render(request,"reg.html",{"form":rform})
        else:return HttpResponse("failed")

    else:
            fo=Registration_form()
            return render(request,'reg.html',{"form":fo})


def home(request):
    return render(request,"home.html")


def contact(request):
    return render(request,"contact.html")


def services(request):
    return render(request,"services.html")

import datetime as dt
date1=dt.datetime.now()
def feedback(request):
    if request.method=='POST':
        fdform=Feedback_from(request.POST)
        if fdform.is_valid():
            name=request.POST.get("name")
            rating=request.POST.get("rating")
            desc=request.POST.get("desc")
            Feedback_model(name=name,rating=rating,desc=desc).save()
            data=Feedback_model.objects.all()

            return render(request,"feedback.html",{'data':data,"fdform":fdform})
        else:
            return HttpResponse("give correct msg")
    else:
        fdform=Feedback_from()
        data=Feedback_model.objects.all()
        return render(request, "feedback.html",{"fdform":fdform,"data":data})


def gallery(request):
    return render(request,"gallery.html")