from django.urls import path, include
from time_jugglers.web.views import index, about, events, discography, store, contact, store_details

urlpatterns = [
    path('', index, name='index'),
    path('discography', discography, name='about'),
    path('events', events, name='events'),
    path('about', about, name='about'),
    path('store/', include([
        path('', store, name='store'),
        path('details/<int:pk>/', store_details, name='store details')
    ])),
    path('contact', contact, name='contact'),
]
