import uuid
from django.db import models
from django.conf import settings


class Community(models.Model):
    """Groups for athletes to connect."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    sport = models.ForeignKey('athletes.Sport', on_delete=models.SET_NULL, null=True, blank=True)
    cover_image = models.ImageField(upload_to='communities/', null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Communities'
    
    def __str__(self):
        return self.name


class CommunityMember(models.Model):
    """Community membership."""
    
    class Role(models.TextChoices):
        MEMBER = 'member', 'Member'
        MODERATOR = 'moderator', 'Moderator'
        ADMIN = 'admin', 'Admin'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='communities')
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['community', 'user']


class Post(models.Model):
    """Community posts."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    """Comments on posts."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']


class Like(models.Model):
    """Likes on posts."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['post', 'user']