from django.shortcuts import render
from .models import Blog
from collections import defaultdict
import operator


def index(request):
    stats = {}

    # Get number of blog posts:
    count = Blog.objects.all().count()
    stats['No. of blogs'] = count

    # Get random keyword frequency
    # 1: Get all tags
    tags = []
    posts = Blog.objects.all()
    for p in posts:
        tags.append(p.tags.names())
    # Flatten
    tags = [val for sublist in tags for val in sublist]

    # 2: Count frequency
    frequency_map = defaultdict(int)
    for t in tags:
        frequency_map[t] += 1

    # 3: Get key with largest val
    largest_key = max(frequency_map.items(), key=operator.itemgetter(1))[0]
    stats['Most mentioned'] = largest_key


    # Latest blog post:
    latest_post = posts.order_by('-date')[0]

    context = {
        'stats': stats,
        'latest_post': latest_post,
    }
    return render(request, 'blog/blog.html', context)