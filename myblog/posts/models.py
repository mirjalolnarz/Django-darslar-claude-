# posts/models.py
from django.db import models

class Post(models.Model):
    title      = models.CharField(max_length=200)
    slug       = models.SlugField(max_length=200, unique=True, blank=True, default='')   # ← yangi
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published  = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']