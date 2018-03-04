from django.shortcuts import render
#from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import NewUserForm

# Create your views here.

def help(request):
   my_ditc = {'insert':'Tech support Help page!'}
   return render(request,'appTwo/help.html',context=my_ditc)


def index(request):
    ditc = {'insert':'Go to /user to for user information!'}
    return render(request,'appTwo/index.html',context=ditc)


def user(request):
   form = NewUserForm()
   
   if request.method == 'POST':
      form = NewUserForm(request.POST)
      
      if form.is_valid():
         form.save(commit=True)
         
         return index(request)
      else:
         print('ERROR FORM INVALID')
         
         
   return render(request,'appTwo/user.html',{'form':form})