from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=400)
    categories = models.ManyToManyField(Category)
    content = tinymce_models.HTMLField()
    timestamp = models.DateTimeField(auto_now=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id,
        })