from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . views import sign_up_view, log_in_view, log_out_view

app_name = 'accounts'


urlpatterns = [
    path('login/', view=log_in_view, name='login'),
    path('logout/', view=log_out_view, name='logout'),
    path('signup/', view=sign_up_view, name='signup'),
]

