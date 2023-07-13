from django.shortcuts import render
from django.contrib import messages #to show alert messages
from django.contrib.auth.models import User #for importing user model
from django.http import HttpResponseRedirect,HttpResponse # for redirecting
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login , logout #for user authentication
from .models import Profile


def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified: #verifying using profile
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password) #if everything correct then it will return userobj and authenticate it
        if user_obj:                                                    #we will create this profile and a signal will be sent
            login(request , user_obj)
            return redirect('/')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')



def register_page(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('first_name')
        email= request.POST.get('email')
        password= request.POST.get('password')

        user_obj= User.objects.filter(username = email)
        #to check if a user already exists
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)#so that it redirects it to the same page

        print(email)
        #if not exists then create user
        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)
    
    return render(request ,'accounts/register.html')


def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')