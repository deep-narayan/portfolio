from django.shortcuts import render
from .model import Messages

def home(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']

		m=Messages(name=name,email=email,subject=subject,message=message)
		m.save()
	return render(request,'index.html')