from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('home/', views.home, name='home'),
    path('university/', views.university_view, name='university'),
    path('pick_department/<str:university>/', views.pick_department_view, name='pick_department'),
    path('papers/', views.papers, name='papers'),
]   