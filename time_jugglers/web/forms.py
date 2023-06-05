from django import forms
from time_jugglers.web.models import Contact


class ContactBaseForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'text']


class ContactCreateForm(forms.ModelForm):
    pass
