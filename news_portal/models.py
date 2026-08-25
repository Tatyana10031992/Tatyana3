from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField("Просмотры", default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.article.title}"


class SavedArticle(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_articles")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="saved_by")

    class Meta:
        unique_together = ("user", "article")


class SiteSettings(models.Model):
    
    background_color = models.CharField(default="#ffffff", max_length=7)
    font_color = models.CharField(default="#000000", max_length=7)
    font_size = models.PositiveIntegerField(default=16)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Profile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    banned_until = models.DateTimeField("Забанен до", null=True, blank=True)

    @property
    def is_banned(self):
        now = timezone.now()
        return self.banned_until and self.banned_until > now

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
