import re
from operator import itemgetter
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project
from.forms import SearchForm


# The index page for the projects. The 'overview'
def index(request):

    template = 'project/projects.html'

    form = SearchForm()

    projects = Project.objects.order_by('-date')[0:2]

    context = {
        'projects': projects,
        'form': form,
    }

    return render(request, template, context)


# The view used to present a page for a single project, Takes a project slug as argument
def single(request, project_slug):
    template = 'project/single.html'
    project = get_object_or_404(Project, slug=project_slug)
    context = {
        'project': project,
        'form': SearchForm(),
    }
    return render(request, template, context)


def search(request):

    # Prepare context (append items later)
    context = {}

    # If method == 'GET', then user has used the search bar
    if request.method == 'GET':

        # Retain the search terms in the search bar
        form = SearchForm(request.GET)

        # If the form is not empty, and input is valid
        if form.is_valid():

            # Regex to extract all the keywords from the search bar input (form.cleaned_data['terms']
            keywords = re.findall("[\w']+", form.cleaned_data['terms'])

            # Get projects with matching tags
            # (need to .distinct() because of the taggit API)
            results = Project.objects.filter(tags__name__in=keywords).distinct()

            # Prepare to return list of 'tuples' (result, matches)
            ret = []

            # Loop through query results
            for r in results:
                # All tags for the resulting object 'r'
                result_tags = r.tags.names()

                # The matching keywords between search terms and the original tags is
                # the intersection between the two sets:
                matches = list(set(result_tags).intersection(set(keywords)))

                # Pair the result r with the intersection and add to the return value
                # (list containing dicts)
                ret.append(
                    {'result': r, 'matches': matches}
                )

            # Sort dict in list by key 'matches'
            # This way the results with most matches are presented first
            sorted_ret = sorted(ret, key=lambda x: len(x['matches']), reverse=True)
            print(sorted_ret)

            # Add the sorted list to the context to return
            context['results'] = sorted_ret
    else:
        form = SearchForm()

    # Add the form to the context
    context['form'] = form

    # Define template to use
    template = 'project/search.html'

    return render(request, template, context)


def archive(request):

    template = 'project/archive.html'
    context = {}

    projects = get_list_or_404(Project.objects.order_by('-date'))

    context['archive'] = projects
    context['form'] = SearchForm()

    return render(request, template, context)
