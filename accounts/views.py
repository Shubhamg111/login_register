from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as auth_login, logout
# from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.views import PasswordResetView
# from django.urls import reverse_lazy



def index(request):
    return render(request,'registration/homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
               auth_login(request, user)
                # Redirect to a specific page after successful login
            return redirect('index')  # Change 'home' to your desired URL name
    else:
            form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    # Redirect to a specific page after logout
    return redirect('login')  # Change 'login' to your desired URL name


# class PasswordReset(PasswordResetView):
#     form_class = PasswordResetForm
#     success_url = reverse_lazy('password_reset_done')
#     email_template_name = 'password_reset_email.html'  # Customize email template

