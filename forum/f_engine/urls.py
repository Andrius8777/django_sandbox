from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('w_engine/', views.thread_list, name='thread_list'),                #def task_list
    path('w_engine/<int:pk>/', views.thread_detail, name='thread_detail'),    #def task_detail
    path('w_engine/post/', views.post_list, name='post_list'),                #def post_list
    path('w_engine/post/<int:pk>/', views.post_detail, name='post_detail'),    #def post_detail
]
