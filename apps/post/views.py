from django.shortcuts import render, redirect
from apps.post.models import Post
from django.db.models import Q 
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(Q(title__icontains=search))[:4]
    else:
        posts = Post.objects.all()[:4]
    context = {
        'posts': posts
        }
    return render(
        request,
        'base.html',
        context
    )

def post(request):
    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(Q(title__icontains=search))
    else:
        posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(
        request,
        'post.html',
        context
    )

def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'post': post
    }
    return render(
        request,
        'post_detail.html',
        context
    )

def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(to='post')

def post_update(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']

            post.title = title
            post.image = image
            post.description = description
            post.save()

            return redirect(to='post')
    context = {
        'form': form
    }
    return render(request, 'pages/update.html', context)

def post_create(request):
    author = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = author
            new_post.save()
        return redirect(to='post')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)

@login_required(login_url='login')
def profile(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'pages/profile.html', context)


@login_required(login_url='login')
def edit(request):
    pk = request.user.id
    user = CustomUser.objects.get(id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            for field in ['first_name', 'last_name', 'icon', 'about']:
                if field in form.cleaned_data:
                    setattr(user, field, form.cleaned_data[field])

            user.save()

            return redirect(to='profile')
    else:
        form = UserForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'icon': user.icon,
            'about': user.about,
        })

    context = {
        'form': form
    }
    return render(request, 'pages/edit.html', context)