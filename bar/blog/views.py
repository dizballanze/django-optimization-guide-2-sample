from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render

from blog.models import Article, Author


class ArticlesListView(ListView):

    template_name = 'blog/articles_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 20
    queryset = Article.objects.select_related('author').prefetch_related('tags').only(
        'title', 'created_at', 'author__username', 'tags__name')


def author_page_view(request, username):
    author = get_object_or_404(Author, username=username)
    return render(request, 'blog/author.html', context=dict(author=author))
