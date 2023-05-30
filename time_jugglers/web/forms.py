from django import forms
from time_jugglers.web.models import Contact


class EmailBaseForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'text']


class EmailCreateForm(forms.ModelForm):
    pass
