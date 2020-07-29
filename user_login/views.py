from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm

def logOut(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("Good bye!")

def validateSessionForm(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'loggedin.html', {'username':username})
    else:
        return render(request, 'login.html', {})

    loginForm = LoginForm()
    return render(request, user_login/validateSessionForm.html, {'form':})
 
def register(request): 
    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thanks for registering</h1></br>")
        response.write("Your username: " + request.POST['username'] + "</br>")
        response.write("Your email: " + request.POST['email'] + "</br>")
        return response 
  
    registerForm = RegisterForm() 
    return render(request, 'user_login/register.html', {'form':registerForm})