from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from .models import Article, Comment, SiteSettings, Profile
from .admin_helpers import admin_required

BAN_PERIODS = {
    "day": timedelta(days=1),
    "week": timedelta(weeks=1),
    "month": timedelta(days=30),
    "forever": timedelta(days=36500),
}


@admin_required
def article_list(request):
    return render(request, "news_portal/admin/article_list.html", {"articles": Article.objects.all()})

@admin_required
def article_create(request):
    if request.method == "POST":
        Article.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            author=request.user
        )
        return redirect("admin_articles")
    return render(request, "news_portal/admin/article_form.html")

@admin_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.save()
        return redirect("admin_articles")
    return render(request, "news_portal/admin/article_form.html", {"article": article})

@admin_required
def article_delete(request, pk):
    Article.objects.filter(pk=pk).delete()
    return redirect("admin_articles")


@admin_required
def user_list(request):
    return render(request, "news_portal/admin/user_list.html", {"users": User.objects.all()})

@admin_required
def user_add(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        return redirect("admin_users")
    return render(request, "news_portal/admin/user_form.html")

@admin_required
def user_delete(request, pk):
    User.objects.filter(pk=pk).delete()
    return redirect("admin_users")

@admin_required
def user_ban(request, pk):
    user = get_object_or_404(User, pk=pk)
    period = request.POST.get("period", "day")
    user.profile.banned_until = timezone.now() + BAN_PERIODS[period]
    user.profile.save()
    return redirect("admin_users")

@admin_required
def comment_delete(request, pk):
    Comment.objects.filter(pk=pk).delete()
    referer = request.META.get("HTTP_REFERER", "/")
    return redirect(referer)


@admin_required
def settings_view(request):
    settings = SiteSettings.load()
    if request.method == "POST":
        settings.background_color = request.POST.get("bg_color", settings.background_color)
        settings.font_color = request.POST.get("font_color", settings.font_color)
        settings.font_size = int(request.POST.get("font_size", settings.font_size))
        settings.save()
        return redirect("admin_settings")
    return render(request, "news_portal/admin/settings.html", {"settings": settings})


@admin_required
def stats(request):
    by_views = Article.objects.order_by("-views")[:10]
    by_comments = Article.objects.annotate(c=Count("comments")).order_by("-c")[:10]
    by_saved = Article.objects.annotate(s=Count("saved_by")).order_by("-s")[:10]

    return render(request, "news_portal/admin/stats.html", {
        "by_views": by_views,
        "by_comments": by_comments,
        "by_saved": by_saved,
    })
