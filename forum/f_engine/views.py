from django.db.models import Count
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #class base views sablonai
from django.views import generic
from django.urls import reverse

def index(request):
    threads = models.Thread.objects.all()
    context = {
        'threads': threads,
        'most_active_member': get_most_active_member(),
    }
    return render(request, 'w_engine/index.html', context)

def get_most_active_member():
    thread_counts = models.Thread.objects.values('creator').annotate(thread_count=Count('creator'))
    most_active_member = max(thread_counts, key=lambda x: x['thread_count'])
    most_active_member_user = get_user_model().objects.get(pk=most_active_member['creator']).username
    return most_active_member_user

def post_list(request):
    post_list = models.Post.objects.all()
    return render(request, 'w_engine/post_list.html', {'post_list': post_list})

def post_detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, 'w_engine/post_detail.html', {'post': post})

class ThreadListView(generic.ListView):
    model = models.Thread
    template_name = 'w_engine/thread_list.html'

class ThreadDetailView(generic.DetailView):
    model = models.Thread
    template_name = 'w_engine/thread_detail.html'