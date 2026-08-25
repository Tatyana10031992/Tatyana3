from django.urls import path
from . import admin_views

urlpatterns = [
    path("admin/", admin_views.article_list, name="admin_dashboard"),
    path("admin/articles/", admin_views.article_list, name="admin_articles"),
    path("admin/articles/create/", admin_views.article_create, name="admin_article_create"),
    path("admin/articles/<int:pk>/edit/", admin_views.article_edit, name="admin_article_edit"),
    path("admin/articles/<int:pk>/delete/", admin_views.article_delete, name="admin_article_delete"),
    path("admin/users/", admin_views.user_list, name="admin_users"),
    path("admin/users/add/", admin_views.user_add, name="admin_user_add"),
    path("admin/users/<int:pk>/delete/", admin_views.user_delete, name="admin_user_delete"),
    path("admin/users/<int:pk>/ban/", admin_views.user_ban, name="admin_user_ban"),
    path("admin/comments/<int:pk>/delete/", admin_views.comment_delete, name="admin_comment_delete"),
    path("admin/settings/", admin_views.settings_view, name="admin_settings"),
    path("admin/stats/", admin_views.stats, name="admin_stats"),
]
