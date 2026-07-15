from django.urls import path,re_path
from . import views

urlpatterns=[
    path('blog-home/', views.home, name="blog-home"),
    path('blog-about/', views.about, name="blog-about"),
    re_path(r'^blog-about/(?P<year>[0-9]{4})/$',views.article_by_year,name="article_by_year"),
    path('blog-about/<int:year>/<str:month>/',views.article_details,name="article_details"),
]