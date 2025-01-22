from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def profile(request):
    return render(request, "users/profile.html")

def posts(request):
    posts = Post.objects.all().order_by("-pk")
    context = {
        "posts": posts,
    }
    return render(request, "posts/posts.html", context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    comments = post.comments.all().order_by("-pk")
    context = {
        "post": post,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "posts/post_detail.html", context)


# 새 글을 생성하고 상세 페이지로 이동
@login_required
def create(request):
    if request.method == "POST":  # 데이터 전송 방식이 POST 일 때
        form = PostForm(request.POST, request.FILES) # form에 request.POST에 있는 데이터 채움, request.FILES에 있는 파일 추가
        if form.is_valid():  # form 형식에 맞으면
            post = form.save(commit=False) # 저장하지 않고 객체 반환
            post.author = request.user # 작성자 추가
            post.save() # 저장
            return redirect('posts:post_detail', post.pk) # 상세 페이지로 이동
    else:                    # 데이터 전송 방식이 POST가 아닐 때
        form = PostForm() # 비어있는 form 생성

    context = {"form": form}
    return render(request, "posts/create.html", context) 
    

# 글 수정(업데이트)
@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:    # 작성자 본인인지 확인
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post) # 강의와 별개로 request.FILES 사진 수정 변경 추가
            if form.is_valid():
                post = form.save()
                return redirect("posts:post_detail", post.pk)
        else:
            form = PostForm(instance=post)

        context = {
            "form": form,
            "post": post,
        }
        return render(request, "posts/update.html", context)
    return redirect('posts:posts')  # 작성자가 아니면 목록으로

# 글 삭제
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:   
        post = get_object_or_404(Post, pk=pk)
        if request.user == post.author:
            post.delete()
            return redirect('posts:post_confirm_delete')
    return redirect('posts:posts')

def post_confirm_delete(request):
    return render(request, 'posts/post_confirm_delete.html')

# 댓글 작성
@require_POST
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    return redirect('posts:post_detail', post_pk)
    

# 댓글 삭제
@require_POST
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('posts:post_detail', post_pk)
# 댓글 삭제 기능 추가하기 22강 숙제 (urls.py와 post_detail에도 추가했음 )

@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)  # 좋아요 취소
            liked = False
        else:
            post.like_users.add(request.user)  # 좋아요
            liked = True
        
        return JsonResponse({'like_count': post.like_users.count(), 'liked': liked})
    
    return JsonResponse({'error': 'Unauthorized'}, status=401)
                    

@login_required
def comment_update(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user != comment.user:
        return redirect('posts:post_detail', post_pk)
        
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    
    context = {
        'form': form,
        'post_pk': post_pk,
        'comment': comment,
    }
    return render(request, 'posts/comment_update.html', context)


    



