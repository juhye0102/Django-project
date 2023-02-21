from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .forms import PostForm
from .models import Post

from datetime import datetime


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
    page = request.GET.get('page')
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
    post.view += 1
    post.save()
    post = get_object_or_404(Post, pk=pk)  # 잘못된 접근에 대한 예외 처리
    return render(request, 'detail.html', {'post': post})


def edit(request, pk):
    edit_post = Post.objects.get(pk=pk)
    return render(request, 'edit.html', {'post': edit_post})


def update(request, pk):
    update_post = Post.objects.get(pk=pk)
    update_post.title = request.POST.get('title')
    update_post.author = request.POST.get('author')
    update_post.content = request.POST.get('content')
    update_post.updated_at = datetime.now()
    update_post.save()
    return redirect('detail', update_post.pk)


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/board/list/')


