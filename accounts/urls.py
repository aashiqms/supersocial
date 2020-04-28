from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('signup/', views.SignUp.as_view(), name='signup'),
]

