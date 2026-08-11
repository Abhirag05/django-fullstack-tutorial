from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('messages/',views.show_messages,name="messages"),
    path('register/',views.register_view,name="register_view"),
    path('login/',views.login_view,name="login_view"),
    path('logout/',views.logout_view,name="logout_view"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('upload/',views.upload_profile,name="upload_profile"),
    path('profile/',views.profile_view,name="profile_view"),
]

