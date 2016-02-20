from django.shortcuts import render, get_list_or_404
from django.core.mail import send_mail
from .forms import ContactForm
from project.models import Project
from blog.models import Blog


def home(request):
    template = 'home.html'

    latest_project = Project.objects.all()[0]
    latest_blog = Blog.objects.all().order_by('date')[0]
    context = {
        'latest_project': latest_project,
        'latest_blog': latest_blog,
    }
    return render(request, template, context)



def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            cc = form.cleaned_data['cc']
            message = form.cleaned_data['message']

            recipients = ['niels@nscp.dk', ]

            if cc:
                recipients.append(email)

            true_subject = ': '.join([name, subject])

            send_mail(true_subject, message, email, recipients, fail_silently=False)

            return render(request, 'thanks.html', context=None)

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)
