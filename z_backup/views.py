from django.db.models import Count
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth import get_user_model

def index(request: HttpRequest) -> HttpResponse:
    thread_counts = models.Thread.objects.values('creator').annotate(thread_count=Count('creator'))
    most_active_member = max(thread_counts, key=lambda x: x['thread_count'])
    most_active_member_user = get_user_model().objects.get(pk=most_active_member['creator']).username
    context = {
        'members_count' : get_user_model().objects.count(),
        'threads_count': models.Thread.objects.count(),         
        'posts_count': models.Post.objects.count(),
        'most_active_member': most_active_member_user,                
    }
    return render(request, 'w_engine/index.html', context)

def thread_list(request: HttpRequest) -> HttpResponse:   #apsirasom nauja funkcija task_list, kad atsirastu pap. menu
    return render(request, 'w_engine/thread_list.html', {   #po sios funkcijos iskart einam apsirasyt tasks/urls.py funkcija
        'thread_list': models.Thread.objects.all(),
    })
    
def post_list(request: HttpRequest) -> HttpResponse:   #apsirasom nauja funkcija task_list, kad atsirastu pap. menu
    return render(request, 'w_engine/post_list.html', {   #po sios funkcijos iskart einam apsirasyt tasks/urls.py funkcija
        'post_list': models.Post.objects.all(),
    })

def thread_detail(request, pk):
    task = get_object_or_404(models.Thread, pk=pk)
    sorted_posts = task.posts.all().order_by('-created_at')
    return render(request, 'w_engine/thread_detail.html', {'task': task, 'sorted_posts': sorted_posts})
    
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:  #apsirasom nauja funkcija task_detail po to i tasks.urls.py
    return render(request, 'w_engine/post_detail.html', {
        'post': get_object_or_404(models.Post, pk=pk),
    })
    


