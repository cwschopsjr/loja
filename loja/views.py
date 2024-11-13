from django.core.paginator import Paginator
from django.shortcuts import render
from loja.models import Post

PER_PAGE = 9


def index(request):
    posts = (
        Post
        .objects
        .filter(is_published=True)
        .order_by('-pk')
    )
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'loja/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request):
    

    return render(
        request,
        'loja/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request):
    

    return render(
        request,
        'loja/pages/post.html',
        {
            # 'page_obj': page_obj,
        }
    )