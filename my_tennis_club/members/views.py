from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from .models import Member
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']


        # Create a new user
        member = Member(email=email, passwort=password, firstname=first_name, lastname=last_name)
        member.save()

    return render(request, 'index.html')

def login_member(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
       
        user = authenticate(request, email=email, passwort=password1)
        print(user)
      
        
        if user is not None:
            login(request, user)
            return redirect('members/details/')  # Hier kannst du deine Weiterleitung anpassen
        else:
            messages.error(request, 'Anmeldung fehlgeschlagen')
            
            return render(request, 'index.html')
    # Falls es sich um einen GET-Request handelt oder um einen Anmeldefehler, zeige das Einloggen-Formular
    return render(request, 'index.html')


def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request)) 
def login(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))



def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))




def main(request):
  template = loader.get_template('main.html')
  
  return HttpResponse(template.render())
 

