from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import CustomUser
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib import messages


def Admin_profile(request):
    # Fetch user profile based on the logged-in user
    try:
        user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('index')  # Redirect to home if user doesn't exist

    context = {
        "user": user,
    }
    return render(request, 'admin/profile/profile.html', context)


def Admin_profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')

        try:
            # Get the current user
            customuser = CustomUser.objects.get(id=request.user.id)
            
            # Update fields if new values are provided
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.email = email
            customuser.username = username

            # If a profile picture is provided, update it
            if profile_pic:
                customuser.profile_pic = profile_pic

            customuser.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('admin_profile')  # Redirect to profile view

        except CustomUser.DoesNotExist:
            messages.error(request, "User profile not found.")
            return redirect('home')  # Redirect to home if user doesn't exist
        
        except Exception as e:
            messages.error(request, f"Profile update failed: {str(e)}")
    
    # If the request method is GET, just render the profile update form
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)



