from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _
from . import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model 
from django.contrib.auth.decorators import login_required

User = get_user_model()

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("AudioForum registration completed."))
            return redirect('login')
    else:
        form = forms.CreateUserForm()
    return render(request, 'u_engine/signup.html', {
        'form': form,
    })
    
@login_required    
def user_detail(request: HttpRequest, username: str | None = None) -> HttpResponse:
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    return render(request, 'u_engine/user_detail.html', {
        'object': user,
    })
    
@login_required
def user_update(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form_user = forms.UserForm(request.POST, instance=request.user)
        form_profile = forms.ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request, _("profile edited successfully").capitalize())
            return redirect('user_detail_current')
    else:
        form_user = forms.UserForm(instance=request.user)
        form_profile = forms.ProfileForm(instance=request.user.profile)
    return render(request, 'user_profile/user_update.html', {
        'form_user': form_user,
        'form_profile': form_profile,
    })