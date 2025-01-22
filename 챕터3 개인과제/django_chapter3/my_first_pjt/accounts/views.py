from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "index"
            return redirect(next_url)
        
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "accounts/login.html", context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("index")


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

@require_POST
def delete(request): # 회원탈퇴
    if request.user.is_authenticated:
        request.user.delete() # auth_logout과 순서 바뀌면 안 됨
        auth_logout(request) # 로그아웃처럼 세션도 삭제
    return redirect("index")

@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)

def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    
    # 자신의 프로필이면 accounts/profile.html을, 다른 사람의 프로필이면 users/users.html을 보여줌
    if request.user.username == username:
        posts = person.posts.all()
        context = {
            'person': person,
            'posts': posts,
        }
        return render(request, 'accounts/profile.html', context)
    else:
        context = {
            'member': person,  # users.html에서 member로 사용중이므로 키 이름을 member로 변경
        }
        return render(request, 'users/users.html', context)


