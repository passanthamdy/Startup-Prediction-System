from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import string
import random

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Post(models.Model):
    user = models.ForeignKey("accounts.CustomUser", related_name="user", on_delete=models.CASCADE)
    category= models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    excerpt = models.TextField()
    slug = models.SlugField(max_length=200,null=False, blank= True, unique=True)
    featured = models.BooleanField(default = False)
    created_at = models.DateTimeField( default= timezone.now)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    user = models.ForeignKey("accounts.CustomUser", related_name="user_com", on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.content

