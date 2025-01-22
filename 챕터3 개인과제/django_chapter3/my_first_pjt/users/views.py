from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


# Create your views here.

@require_POST
@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = get_object_or_404(User, pk=user_pk)
    me = request.user

    if me != you:
        if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', you.username)
