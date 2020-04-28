from django.urls import path

from .views import create_post_view, delete_post_view, post_detail_view, user_post_view, post_list_view

app_name = 'posts'

urlpatterns = [
    path("", view=post_list_view, name="all"),
    path("new/", view=create_post_view, name="create"),
    path("by/<username>/", view=user_post_view, name="for_user"),
    path("by/<username>/<int:pk>/", view=post_detail_view, name="single"),
    path("delete/<int:pk>/", view=delete_post_view, name="delete"),
]
