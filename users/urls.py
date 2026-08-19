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
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('delete-session/', views.delete_session, name='delete_session'),
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),
    path('send-email/', views.send_email, name='send_email'),
    path('send-html-email/', views.send_html_email, name='send_html_email'),
    path('send-bulk-email/', views.send_bulk_email, name='send_bulk_email'),
    path('send-bulk-html-email/', views.send_bulk_html_email, name='send_bulk_html_email'),
]

