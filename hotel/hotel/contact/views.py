from django.shortcuts import render,redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from .forms import contactform

# Create your views here.
def send_email(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['name']
            from_email=form.cleaned_data['from_email']
            message=form.cleaned_data['message']


            try:
                send_mail(subject,message,from_email,['admin@example.com'])
            except BadHeaderError:
                return HttpResponse("inavlid header")
            
            return redirect("contact:send_success")

    else:
        form = contactform()
    
    context={'form':form}

    return render(request,'contact.html',context)
  



def send_success(request):
  return HttpResponse("thanks")