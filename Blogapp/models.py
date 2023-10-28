from django.db import models
#now to import user class
from django.contrib.auth.models import User
# Create your models here.

#we gonna create tuple 0 for draft and 1 for publish
STATUS = ((0, "Draft"), (1,"published"))
   
#let's create a class 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS,default=0)


    
    class Meta:
     #meta for different ascending or descending order
      ordering = ['-created_on']
  
    def __str__(self):
       return self.title
    
    



    

