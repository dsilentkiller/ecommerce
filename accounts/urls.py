from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
# from accounts.views import LoginView
app_name = 'accounts'
urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),
    path('login/', views.RegisterView.as_view(), name='register'),
     path('login/', views.PasswordChangeView.as_view(), name='register'),

]
