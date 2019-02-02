from django.urls import re_path, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    re_path(
        r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        views.activate, name='activate'
    ),
    path(r'register/', views.register, name='register'),
    path(
        r'login/', auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
]
