from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class ForumMember(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    skills = models.CharField('skills', blank=True, max_length=100, db_index=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Forum Member"
        verbose_name_plural = "Forum Members"
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("forum_member_detail", kwargs={"pk": self.pk}) 
      

class Thread(models.Model):
    title = models.CharField('title', blank=True, max_length=200, db_index=True)
    created_at = models.DateTimeField("created at", auto_now_add=True, db_index=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='threads', default=None)

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("thread_detail", kwargs={"pk": self.pk})  
         

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts', default=None )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Post by {self.author.username} in {self.thread.title}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
