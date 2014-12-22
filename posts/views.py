from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from posts.models import Post
# Create your views here.
import datetime

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'posts/detail.html', {'post': post})

def create(request):
    post = Post(post_text=request.POST['post_text'], title=request.POST['title'], content=request.POST['content'], pub_date=datetime.datetime.now())
    post.save()
    return HttpResponseRedirect(reverse('posts:detail', args=(post.id,)))

def publish(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.publish()
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'posts/detail.html', {'post': post})

def unpublish(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.unpublish()
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'posts/detail.html', {'post': post})