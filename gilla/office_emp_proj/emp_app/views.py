from django.http import HttpResponse
from django.shortcuts import render
from .models import FeedBack_Form
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=="POST":
        feedback_form=FeedBack_Form()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        feedback_form.name=name
        feedback_form.email=email
        feedback_form.subject=subject
        feedback_form.save()
        return HttpResponse("<h1>THANKS FOR YOUR VALUABLE TIME</h1>")

    return render(request,'index.html')
   