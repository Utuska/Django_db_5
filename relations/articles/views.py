from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Principal


def articles_list(request):
    template = 'articles/new.html'

    article = Article.objects.all()
    principal = Principal.objects.all()
    #ordering = '-published_at'
    #order_by('-published_at')

    context = {'object_list': article, 'status': principal}
    return render(request, template, context)
