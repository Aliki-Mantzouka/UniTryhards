from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.profile_view, name='profile')
]