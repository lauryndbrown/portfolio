from django.db import models

class BlogPost(models.Model):
   title = models.CharField(max_length = 60)
   sub_title = models.CharField(max_length = 200)
   pub_date = models.DateTimeField('date published')
   image = models.ImageField(upload_to='blog')
   body = models.TextField()
   

class PostComment(models.Model):
   poster_name = models.CharField(max_length = 60)
   body = models.TextField()
   blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
   pub_date = models.DateTimeField('date published')
