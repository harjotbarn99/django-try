from django.urls import path
from .views import ArticleListView,ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = "blogy"

urlpatterns=[
    path("", ArticleListView.as_view(),name="allArticles"),
    path("<int:id>/", ArticleDetailView.as_view(),name="particularBlog"),
    path("create/", ArticleCreateView.as_view(), ),
    path("<int:id>/update/", ArticleUpdateView.as_view(),),
    path("<int:id>/del/", ArticleDeleteView.as_view(),),



]