from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreateForm, PostPictureForm,ProfileUpdateForm, CommentForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Profile, Image



@login_required
def landing(request):
    image = Image.objects.all()
  
    return render(request,'index.html', {'image': image})


@login_required               
def profile(request):
    
    return render(request, 'profile.html',)


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'update_profile.html', context)


@login_required
def image_form(request):

    if request.method == 'POST': 
        form = PostPictureForm(request.POST, request.FILES) 
  
        if form.is_valid():
            form.save()
            return redirect('landing') 
    else: 
        form = PostPictureForm() 
    return render(request, 'image_form.html', {'form' : form}) 


def post_detail(request):
    template_name = 'post_detail.html'
    # post = get_object_or_404(Post)
    posts = Post.objects.all()    
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.topic = topic
            form.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'posts': posts,  'new_comment': new_comment, 'comment_form': comment_form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('profile.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request, template_name = "registration/login.html", context={"form":form})  