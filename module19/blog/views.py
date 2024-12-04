from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    page_size = request.GET.get('page_size', 5)
    paginator = Paginator(posts, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'page_size': page_size,

    }
    return render(request, 'blog/post_list.html', context)


def news_list(requset):
    return render(requset, 'blog/post_list.html')
