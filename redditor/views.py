from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm, PostPictureForm, UserUpdateForm, ProfileUpdateForm, CommentForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Profile, Image



@login_required
def landing(request):
    
  
    return render(request,'index.html')


@login_required
def profile(request):
    # if request.method == 'POST':
    #     user_form = UserUpdateForm(request.POST)
    #     profile_form = ProfileUpdateForm(request.POST, request.FILES)

    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')

    # else:
    #     user_form = UserUpdateForm()
    #     profile_form = ProfileUpdateForm()

    # context = {
    #     'u_form': user_form,
    #     'p_form': profile_form
    # }

    return render(request, 'profile.html')


@login_required
def update_profile(request):
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'update_profile.html', context)