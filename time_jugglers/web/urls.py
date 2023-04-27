from django.urls import path, include

urlpatterns = [
    path('', """index""", name='index'),
    path('discography', """discography""", name='about'),
    path('events', """events""", name='events'),
    path('about', """about""", name='about'),
    path('store', """store""", name='store'),
    path('contact', """contact""", name='contact'),
]