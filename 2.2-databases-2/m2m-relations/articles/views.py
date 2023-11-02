from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {'object_list':Article.objects.all().order_by(ordering)}

    return render(request, template, context)
