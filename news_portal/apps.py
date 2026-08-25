from django.apps import AppConfig
from django.db.models.signals import post_migrate


class NewsPortalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news_portal"

    def ready(self):
        post_migrate.connect(create_admin_group, sender=self)


def create_admin_group(sender, **kwargs):
    # Импорты внутри функции — чтобы Django успел загрузиться
    from django.contrib.auth.models import Group, Permission

    group, created = Group.objects.get_or_create(name="Администратор")
    if created:
        perms = Permission.objects.filter(codename__in=[
            "add_article", "change_article", "delete_article",
            "add_user", "delete_user", "change_user",
            "delete_comment", "view_article"
        ])
        group.permissions.set(perms)
