from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post

from datetime import datetime, timezone


# 메인 화면
def index(request):
    template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date': now
    }
    
    return HttpResponse(template.render(context, request))


# (임시)전체 게시글 조회
def list(request):
    template = loader.get_template('list.html')
    context = {
        'items': Post.objects.all()
    }
    return HttpResponse(template.render(context, request))


# 게시글 작성
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  
        if form.is_valid():  
            new_item = form.save()  
        return HttpResponseRedirect('/board/list/') 
    form = PostForm()
    return render(request, 'create.html', {'form': form})


# 게시글 상세 보기
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)  # 잘못된 접근에 대한 예외 처리
    return render(request, 'detail.html', {'post': post})


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'edit.html', {'post': post})


def update(request, pk):
    post = Post.objects.get(pk=pk)
    post.title = request.POST.get('title')
    post.author = request.POST.get('author')
    post.content = request.POST.get('content')
    post.updated_at = datetime.now()
    post.save()
    return render(request, 'detail.html', update.pk)


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/board/list/')
