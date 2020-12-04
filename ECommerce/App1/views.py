from django.shortcuts import render
from App1.forms import UserInfoForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
#Return Homepage of the products
def index (request):
    return render(request, 'APP1/index.html')

def register (request):
    #Check if the form is submitted
    #registered = False
    Tryagain = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        userinfo_form = UserInfoForm(data = request.POST)
        if user_form.is_valid() and userinfo_form.is_valid():
            #Saving the new user
            user = user_form.save()
            #Hashing the password then save it
            user.set_password(user.password)
            user.save()

            #Save userinfo to database after ensuring that the data is stored to the same user
            userinfo = userinfo_form.save(commit = False)
            userinfo.user = user
            userinfo.save()
            #Put registered = true to change the view of the homepage for the registered users
            #reistered = True
            return render(request, 'App1/login.html')
        else:
            #Tryagain allows making changes to the register.html page
            Tryagain = True
            user_form = UserForm()
            userinfo_form = UserInfoForm()
            return render(request, 'App1/register.html', {'user_form' : user_form,'userinfo_form' : userinfo_form, 'Tryagain' : Tryagain})

    #Send the form details to register.html file
    else:
        user_form = UserForm()
        userinfo_form = UserInfoForm()
        return render(request, 'App1/register.html', {'user_form' : user_form,'userinfo_form' : userinfo_form, 'Tryagain' : Tryagain })

#Login view
def user_login(request):
    WrongPassword = False #Variable used to display error message to the user if login failed
    if request.method == 'POST':
        #Get the inputted data in login form
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Check the correctness of data
        user = authenticate(username=username, password=password)

        #If the data is correct
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'App1/index.html')
            else:
                WrongPassword = True
                return render(request, 'App1/login.html', {'WrongPassword': WrongPassword})
        else:
            WrongPassword = True
            return render(request, 'App1/login.html', {'WrongPassword': WrongPassword})

    #Send the form details to login.html file
    else:
        return render(request, 'App1/login.html', {'WrongPassword': WrongPassword})

#Logout view
@login_required      #This function isn't executed except if the user is logged in
def user_logout(request):
    logout(request)
    return render(request, 'App1/index.html')
