from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from main.models import CustomUser

def admin_profile(request):
    user = get_object_or_404(CustomUser, pk=request.user.pk)
    return render(request, 'profile.html', {'user': user})

def admin_profile_update(request):
    if request.method == "POST":
        profile_picture = request.FILES.get('profile_picture')  # must match input name
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            customuser = CustomUser.objects.get(pk=request.user.pk)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if profile_picture:
                customuser.profile_picture = profile_picture

            customuser.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('admin_profile')

        except CustomUser.DoesNotExist:
            messages.error(request, "User profile not found.")
            return redirect('dashboard')

        except Exception as e:
            messages.error(request, f"Profile update failed: {str(e)}")
            return redirect('admin_profile')

    return redirect('admin_profile')
