from django.shortcuts import render , get_object_or_404 , redirect
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm
from django.urls import reverse


# Create your views here.
class ArticleDeleteView(DeleteView):
    template_name = "blogy/deleteBlogy.html"
    # queryset = Article.objects.all( )

    def get_object(self, queryset=None):
        idC = self.kwargs.get("id")
        return get_object_or_404(Article,id = idC)

    def get_success_url(self):
        return reverse("blogy:allArticles")



class ArticleListView(ListView):
    template_name = "blogy/mainblogy_view.html"
    queryset = Article.objects.filter(active=True)

class ArticleDetailView(DetailView):
    template_name = "blogy/detailBlogy.html"
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        idC = self.kwargs.get("id")
        return get_object_or_404(Article,id = idC)


class ArticleCreateView(CreateView):
    template_name = "blogy/createBlogy.html"
    form_class =  ArticleForm
    queryset = Article.objects.all()
    # success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = "blogy/createBlogy.html"
    form_class =  ArticleForm
    queryset = Article.objects.all()
    #success_url = "/"

    def get_object(self, queryset=None):
        idC = self.kwargs.get("id")
        return get_object_or_404(Article,id = idC)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)