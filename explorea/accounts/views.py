from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    
    return render(request, 'accounts/profile.html')


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data.get('password1')
            
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('profile')
        else:
            return render(request, 'accounts/register.html', {'form': form} )

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form} )

@login_required
def edit_profile(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            return redirect('profile')

    form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form} )

@login_required
def change_password(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/accounts/profile/')
        else:
            return render(request, 'accounts/change_password.html', {'form': form})

    form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})