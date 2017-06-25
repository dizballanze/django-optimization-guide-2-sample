from django.conf.urls import url

from blog.views import ArticlesListView


urlpatterns = [
    url(r'^$', ArticlesListView.as_view(), name='articles_list'),
]
