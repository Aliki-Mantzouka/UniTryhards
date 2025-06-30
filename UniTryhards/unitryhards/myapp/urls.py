from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('home/', views.home, name='home'),
    path('university/', views.university_view, name='university'),  # University selection
    path('department/<int:university_id>/', views.department_view, name='department'),  # Department selection
    path('course_selection/<int:university_id>/<int:department_id>/', views.course_selection_view, name='course_selection'),
    path('papers/<int:department_id>/<int:course_id>/', views.papers_view, name='papers'),  # Shows all papers for a course
    path('papers/<int:department_id>/<int:course_id>/category/<str:category>/', views.papers_by_category_view, name='papers_by_category'),
    path('papers/<int:department_id>/<int:course_id>/<int:paper_id>/', views.paper_detail_view, name='paper_detail'),  # Shows detailed view of a single paper
    path('upload/', views.upload_paper_view, name='upload_paper'),
    path('papers/<int:department_id>/<int:course_id>/<int:paper_id>/', views.paper_detail_view, name='paper_detail'),
    path('papers/<int:paper_id>/report/', views.report_paper, name='report_paper'),
    path('papers/<int:paper_id>/toggle_favorite/', views.toggle_favorite_paper, name='toggle_favorite_paper'),
    path('paper/<int:paper_id>/view/', views.view_paper, name='view_paper'),
    path('paper/<int:paper_id>/download/', views.download_paper, name='download_paper'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)