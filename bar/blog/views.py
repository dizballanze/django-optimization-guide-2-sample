from django.views.generic import ListView

from blog.models import Article


class ArticlesListView(ListView):

    template_name = 'blog/articles_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 20
    queryset = Article.objects.select_related('author')
