from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from marketing.models import Signup

def index(request):
    featured_index = Post.objects.filter(featured=True)
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    gallery_posts = Post.objects.order_by('-timestamp')[0:4]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured_index,
        'latest_posts': latest_posts,
        'gallery': gallery_posts,
    }
    return render(request, 'index.html', context)

def blog(request):
    post_list = Post.objects.all()
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    paginator = Paginator(post_list, 4)

    # Getting requested page number
    page_requested_var = 'page'
    page = request.GET.get(page_requested_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'latest_posts': latest_posts,
        'page_number': page_requested_var,

    }
    return render(request, 'blog.html', context)

def post(request, id):
    return render(request, 'post.html', {})