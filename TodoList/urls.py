from django.contrib import admin
from django.urls import path, include
from todo.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('todo/', include('todo.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Allow GET requests for logout (less secure, but avoids 405 error)
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/', admin.site.urls),
]
