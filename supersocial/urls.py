from django.contrib import admin
from django.urls import path, include
from . views import home_page_view, test_page_view, thanks_page_view

app_name = 'accounts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=home_page_view, name='home'),
    path('accounts', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', view=test_page_view, name='test'),
    path('thanks/', view=thanks_page_view, name='thanks'),
]

