from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Posts
from .forms import PostForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .decorators import unauthenticated_user, allowed_users
from django.views.decorators.http import require_GET


def home(request):
    return redirect('posts')

#all published posts
def posts(request):
    posts = Posts.objects.filter(publish=True).order_by("-pk")
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)

#all unpublished posts
@staff_member_required(login_url="login")
def unpublishedposts(request):
    unpublishedposts = Posts.objects.filter(publish=False)
    context = {'unpublishedposts': unpublishedposts}
    return render(request, 'base/unpublishedposts.html', context)


#single post(article)
def article(request, slug):
    article = Posts.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'base/article.html', context)




#post creating form
@staff_member_required(login_url="login")
def CreateForm(request):  
    form = PostForm

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}

    return render(request, 'base/post_form.html', context)

#update published form
@allowed_users(allowed_roles=['Editor', 'Admin'])
def UpdateForm(request, slug):
    post = Posts.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}

    return render(request, 'base/post_form.html', context)
#update unpublished article form
@staff_member_required(login_url="login")
def UnpublishedUpdateForm(request, slug):
    
    post = Posts.objects.filter(publish=False).get(slug=slug)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}

    return render(request, 'base/post_form.html', context)
#Delete Posts
@allowed_users(allowed_roles=['Admin'])
def DeleteForm(request, slug):

    post = Posts.objects.get(slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect('posts')

    context = {'item': post}

    return render(request, 'base/delete.html', context)
#user registration
@unauthenticated_user
def RegisterPage(request):

    form = CreateUserForm()

    
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get( 'last_name')
            messages.success(request, 'Account Create Successfully for '+ first_name + ' ' + last_name + ' with username '+username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'base/register.html', context)

#user login
@unauthenticated_user
def LoginPage(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is invalid')

    context = {}
    return render(request, 'base/login.html', context)

#user logout
@login_required(login_url="login")
def LogoutUser(request):
    logout(request)
    return redirect('login')



#change password
@login_required(login_url="login")
def User_ChangePassword(request):
    if request.method == 'POST':
        pwchangeform = PasswordChangeForm(user=request.user, data=request.POST)
        if pwchangeform.is_valid():
            pwchangeform.save()
            return redirect('home')
    else:
        pwchangeform = PasswordChangeForm(user=request.user)
    context = {'form':pwchangeform}
    return render(request, 'base/changepassword.html', context)


#robots txt
@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",#allows all search engine crawler to crawl
        "Allow: /To allpw/",
        "Disallow: /To disallow/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

