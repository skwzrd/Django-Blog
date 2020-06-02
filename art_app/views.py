from django.shortcuts import render, redirect

from .models import Post

PAGE_POSTS = 15

def index(request):
    """Shows posts numbered 0 to PAGE_POSTS"""
    return index_page(request, 0)


def index_page(request, page: int = 0):
    """Shows posts numbered N to N + PAGE_POSTS"""
    posts = Post.objects.all()
    post_count = posts.count()

    lower = page*PAGE_POSTS
    upper = lower + PAGE_POSTS

    if page*PAGE_POSTS > post_count or page < 0:
        return redirect('art_app:index_page')

    post_list = posts[lower : upper]
    prev_page = page-1 if page >= 1 else None
    next_page = page+1 if post_count > page*PAGE_POSTS + PAGE_POSTS else None

    pages = {'prev': prev_page, 'next': next_page}
    context = {'post_list': post_list, 'pages': pages}

    return render(request, 'art_app/index.html', context)

