from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

class BlogPost(models.Model):
  title=models.CharField(max_length=200)
  slug = models.SlugField(unique=True)
  author=models.ForeignKey(User,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
