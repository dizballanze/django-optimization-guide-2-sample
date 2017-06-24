from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Author(models.Model):

    username = models.CharField(max_length=64)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateField()
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag)
    comments_on = models.BooleanField(default=True)

    def __str__(self):
        return self.title
