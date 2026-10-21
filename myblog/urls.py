
from django.contrib import admin
from django.urls import path, include 
from . import views
from django.contrib.auth import views as auth_views
from blog.views import signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/", signup, name="signup"),
]
