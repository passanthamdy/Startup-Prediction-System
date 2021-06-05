from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import string
import random
from location_field.models.plain import PlainLocationField
from django.contrib.postgres.fields import ArrayField

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class Post(models.Model):
    user = models.ForeignKey("accounts.CustomUser", related_name="post", on_delete=models.CASCADE)
    profile = models.ForeignKey("profiles.Profile",related_name='profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    excerpt = models.TextField()
    image = models.ImageField( upload_to=upload_to, default = 'def.png')
    slug = models.SlugField(max_length=200,null=True, blank= True, unique=True)
    likes = models.ManyToManyField("accounts.CustomUser", related_name= 'likes', blank=True)
    featured = models.BooleanField(default = False)
    created_at = models.DateTimeField( default= timezone.now)

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()


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


class Dataset(models.Model):
    user = models.ForeignKey("accounts.CustomUser" , on_delete=models.CASCADE)
    category_list= models.CharField( max_length=50)
    country_code = models.CharField( max_length=50)
    funding_total_usd = models.FloatField()
    funding_rounds = models.IntegerField()
    score=models.FloatField()
    maxfund=models.FloatField()
    minfund=models.FloatField()
    status=models.BooleanField()


