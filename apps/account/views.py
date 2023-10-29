from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Successful authentication')
                else:
                    return HttpResponse('Account does not exist')
            else:
                HttpResponse('Wrong login')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1']
            )
            new_user.save()
            context = {
                'new_user': new_user
            }
            return render(
                request,
                'account/register_done.html',
                context
            )

    if request.method == 'GET':
        user_form = UserRegistrationForm()
    context = {
        'user_form': user_form
    }
    return render(request, 'account/register.html', context)


