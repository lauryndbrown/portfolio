from django.contrib import admin
from mysite.models import BlogPost
 
class BlogPostAdmin(admin.ModelAdmin):
        list_display = ['title','sub_title']
        list_filter = ['pub_date']
        search_fields = ['title', 'sub_title', 'body']
        date_hierarchy = 'pub_date'
        save_on_top = True
admin.site.register(BlogPost, BlogPostAdmin)
