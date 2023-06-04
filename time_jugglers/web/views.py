from time_jugglers.web.forms import EmailCreateForm
from django.shortcuts import render, redirect
from django.utils import timezone
from time_jugglers.web.models import Event, Product


def index(request):
    return render(
        request,
        'home.html',
    )


def about(request):
    return render(
        request,
        'about.html',
    )


def discography(request):
    return render(
        request,
        'discography.html',
    )


def events(request):
    context = {
        'events': Event.objects.all()
    }

    return render(
        request,
        'events.html',
        context
    )


def store(request):
    context = {
        'products': Product.objects.all()
    }

    return render(
        request,
        'store/store.html',
        context,
    )


def contact(request):
    if request.method == 'GET':
        form = EmailCreateForm()
    else:
        form = EmailCreateForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.date_sent = timezone.now()
            email.save()
            return redirect('contact')

    context = {
        'form': form,
    }

    return render(
        request,
        '',
        context
    )
