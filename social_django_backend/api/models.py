import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True)
    bio = models.TextField(null=True)
    email = models.EmailField(unique=True, null=True)
    profile_image = models.ImageField(upload_to='uploads/avatars', null = True)
    cover_image = models.ImageField(upload_to='uploads/covers', null = True)
    hashed_password = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    following_users = models.ManyToManyField('self', symmetrical=False)
    has_notification = models.BooleanField(default=False)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    liked_users = models.ManyToManyField(User, related_name='liked_posts')
    bookmarked_users = models.ManyToManyField(User, related_name='bookmarked_posts')
    image = models.TextField(null=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
