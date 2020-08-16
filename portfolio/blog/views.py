from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def blog_index(request):
    # -sign means we render posts ordered by the most recent
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    #comment posted
    if request.method=="POST":

       form_class=Commentform(request.POST)

       if form_class.is_valid(): 
           #create commnt object but dont save to the database yet
           new_c=form_class.save(commit=False)
           #assign the current post to the comment
           new_c.post=post
           #save the comment to the database
           new_c.save()
           
    else:
        form_class=Commentform()
    context = {
        "post": post,
        "comments": comments,
        'form':form_class,
    }

    return render(request, "blog/blog_detail.html", context)
