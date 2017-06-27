from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Author(models.Model):

    username = models.CharField(max_length=64, db_index=True)
    email = models.EmailField()
    bio = models.TextField()
    articles_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Article(models.Model):

    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateField()
    author = models.ForeignKey(Author, related_name='articles')
    tags = models.ManyToManyField(Tag)
    comments_on = models.BooleanField(default=True)

    def __str__(self):
        return self.title
