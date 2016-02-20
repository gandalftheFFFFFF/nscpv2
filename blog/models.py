from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    slug = models.SlugField()
    tags = TaggableManager()
    description = models.CharField(max_length=200)
    body = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']