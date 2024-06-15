from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return reverse('article_details', args=(str(self.id)))
        return reverse('home')




class profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
    website_url=models.CharField(max_length=255,null=True,blank=True)
    fb_url=models.CharField(max_length=255,null=True,blank=True)
    twitter_url=models.CharField(max_length=255,null=True,blank=True)
    instagram_url=models.CharField(max_length=255,null=True,blank=True)
    pinterest_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)
    


class post(models.Model):
    title=models.CharField(max_length=300)
    header_image=models.ImageField(null=True,blank=True,upload_to='images/')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    # body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    category =models.CharField(max_length=255,default='coding')
    likes=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} | {self.author.username}"
    
    def get_absolute_url(self):
        # return reverse('article_details', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    Post=models.ForeignKey(post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=277)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return '%s - %s' % (self.Post.title,self.name)
