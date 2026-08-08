from django.urls import path,re_path
from . import views

app_name="blog"

urlpatterns=[
    path('blog-home/', views.home, name="blog-home"),
    path('blog-about/', views.about, name="blog-about"),
    re_path(r'^blog-about/(?P<year>[0-9]{4})/$',views.article_by_year,name="article_by_year"),
    path('blog-about/<int:year>/<str:month>/',views.article_details,name="article_details"),
    path('article-filter/',views.article_filter,name="article_filter"),
    path('create-blog/',views.create_blog,name="create_blog"),
    path('blog-list/',views.blog_list,name="blog_list"),
    path('blog-detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog-edit/<int:pk>/', views.blog_edit, name='blog_edit'),
]