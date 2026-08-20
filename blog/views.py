from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .forms import BlogForm
from django.contrib import messages
from .models import Blog 
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.cache import cache
from django.views.decorators.cache import cache_page

# Create your views here.
def home(request):
    return render(request,'blogs/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the blog about page.")

def article_by_year(request,year):
    return HttpResponse(f"Article from the year: {year}")

def article_details(request,**kwargs):
    return HttpResponse(f"Article from the year: {kwargs['year']} and month:{kwargs['month']}")

#Filters example
@cache_page(30)  # dedicated file based cach implementation for a single view using decorators.Cache the view for 30 seconds
def article_filter(request):
    print("hitting the article filter view from the database")
    blogs=[
        {"title": "Blog 1", "is_featured": True, "author": "Author 1"},
        {"title": "Blog 2", "is_featured": False, "author": "Author 2"},
        {"title": "Blog 3", "is_featured": False, "author": "Author 3"}
    ]
    post_list ={
            "blogs": blogs,
            "title": "Post 1",
            "author": "Author 1",
            "date": datetime(2025, 8, 1),
            "content": "This is the content of the post.",
            "price": 100,
            "test": "<b>Auto escape example</b>",
        }
    return render(request, 'blogs/article_filter.html', {'post_list': post_list})

"""def create_blog(request):
    form=BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog created successfully!")
            return redirect('blog:blog_list')
    return render(request, 'blogs/create_blog.html', {'form': form}) """

#class based views for creating the blog
class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/create_blog.html'
    success_url = '/blog/blog-list/'


"""def blog_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    if query:
        blogs = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    elif category:
        blogs = Blog.objects.filter(category__iexact=category)
    else:
        blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)  # Show 2 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/blog_list.html', 
    {
        'page_obj': page_obj,
        'query': query,
        'category': category
    }
    ) """

#Class based views for listing the blogs

class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if query:
            return Blog.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        elif category:
            return Blog.objects.filter(category__iexact=category)
        else:
            #using of inmemory caching/file based caching to store the blogs for 300 seconds to reduce the database hits and improve performance
            cached_blogs = cache.get('blogs')
            if cached_blogs is None:
                print("Cache miss: Fetching blogs from database")
                cached_blogs = Blog.objects.all()
                cache.set('blogs', cached_blogs, 300)  # Cache for 300 seconds
            else:
                #print("Cache hit: Using cached blogs")
                print("Cache hit: Using file-based cached blogs")
            return cached_blogs

"""
def blog_detail(request, pk):
    blog=get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog}) """

#class based views for blog detail
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'


"""def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully!")
            return redirect('blog:blog_list')
    return render(request, 'blogs/create_blog.html', {'form': form}) """

#class based views for blog edit
class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/create_blog.html'
    success_url = '/blog/blog-list/'

"""def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Blog deleted successfully!")
        return redirect('blog:blog_list')
    return render(request, 'blogs/blog_delete.html', {'blog': blog}) """

#class based views for blog delete
class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = '/blog/blog-list/'
