from django.urls import path
from . import views             # 이 곳은 posts 앱의 URL 입니다.

app_name = 'posts'
urlpatterns = [
    path("", views.posts, name="posts"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:post_pk>/comments/", views.comment_create, name="comment_create"),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', 
        views.comment_delete, 
        name='comment_delete'
    ), 
    path("<int:pk>/like/", views.like, name="like"), 
    path("profile/", views.profile, name="profile"),
    path("post_confirm_delete/", views.post_confirm_delete, name="post_confirm_delete"),
    path('<int:post_pk>/comments/<int:comment_pk>/update/', 
        views.comment_update, 
        name='comment_update'
    ),
]