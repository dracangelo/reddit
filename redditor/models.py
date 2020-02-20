from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime as dt
from PIL import Image

# # Create your models here.


class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to = 'redditss', null=False)
    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts
    def save_post(self):
        self.save()
    def delete_post(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'redditss')
    caption = models.CharField(max_length=300)
    date_posted = models.DateField(default=timezone.now)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=255)
    date_posted = models.DateField(default=timezone.now)
    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='redditss')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



    

