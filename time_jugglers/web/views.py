from time_jugglers.web.forms import EmailCreateForm
from django.shortcuts import render, redirect
from django.utils import timezone


def index(request):
    return render(
        request,
        'time_jugglers_website/templates/home.html',
    )


def about(request):
    return render(
        request,
        'time_jugglers_website/templates/about.html',
    )


def discography(request):
    return render(
        request,
        'time_jugglers_website/templates/discography.html',
    )


def contact_create(request):
    if request.method == 'GET':
        form = EmailCreateForm()
    else:
        form = EmailCreateForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.date_sent = timezone.now()
            email.save()
            return redirect('contact sent')

    context = {
        'form': form,
    }

    return render(
        request,
        '',
        context
    )
