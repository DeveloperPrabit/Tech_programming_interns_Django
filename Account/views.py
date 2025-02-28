from django.contrib import messages
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, "Account/login.html")


#for registration:
def RegisterPage(request):
    if request.method == "POST":
        # Retrieve form data
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check if passwords match
        if password1 == password2:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken!")  # Red error message
                return redirect("RegisterPage")

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")  # Red error message
                return redirect("RegisterPage")

            # Create the new user
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            # Log the user in
            login(request, user)

            # Success message and redirect to login page
            messages.success(request, "Registration successful! You are now logged in.")  # Green success message
            return redirect("LoginPage")  # Replace with the name of your login page or dashboard

        else:
            # Passwords don't match
            messages.error(request, "Passwords do not match!")  # Red error message
            return redirect("RegisterPage")

    # Render the registration page template
    return render(request, "Account/register.html")

def Log_out(request):
    logout(request)
    return redirect('index')  # Replace 'home' with your actual URL name
