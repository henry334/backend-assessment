from django.shortcuts import render
from .models import BlogPost, Tag

def blog_list(request):
    tags = Tag.objects.all()
    tag_id = request.GET.get('tag_id')
    if tag_id:
        posts = BlogPost.objects.filter(tags__id=tag_id) # Search for posts with the tag_id
    else:
        posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts, 'tags': tags})