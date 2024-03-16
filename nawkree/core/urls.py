from django.urls import path
from . import views as custom_views
from django.contrib.auth import views

urlpatterns = [
    path('logout/', custom_views.custom_logout, name='logout'),
    path('signup/', custom_views.signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
]
