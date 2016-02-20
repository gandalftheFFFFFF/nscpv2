from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    short_description = models.CharField(max_length=200)
    url = models.URLField(max_length=300, blank=True, null=True)
    tags = TaggableManager()
    long_description = RichTextField()
    date = models.DateField()

    def __str__(self):
        return self.title
