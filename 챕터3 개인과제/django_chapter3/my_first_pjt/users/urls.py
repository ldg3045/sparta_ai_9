from django.urls import path
from . import views          # 이 곳은 users 앱의 URL 입니다.

app_name = 'users'
urlpatterns = [
    path("follow/<int:user_pk>/", views.follow, name="follow"),
]

