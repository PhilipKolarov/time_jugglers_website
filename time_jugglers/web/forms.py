from django import forms
from time_jugglers.web.models import Contact, Order


class ContactBaseForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'text']


class ContactCreateForm(ContactBaseForm):
    pass


class OrderBaseForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'city', 'country', 'quantity', 'size']


class OrderCreateForm(OrderBaseForm):
    pass
