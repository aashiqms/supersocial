from django.urls import path
from .views import list_group_view, single_group_view, create_group_view, join_group_view, leave_group_view

app_name = 'accounts'
urlpatterns = [
    path('', view=list_group_view, name='all'),
    path('new/', view=create_group_view, name='create'),
    path('posts/in/<slug>/', view=single_group_view, name='single'),
    path('join/<slug>/', view=join_group_view, name="join"),
    path('leave/<slug>/', view=leave_group_view, name="leave"),
]

