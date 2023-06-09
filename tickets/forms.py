from django import forms

from tickets.models import Ticket


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
          "description": forms.Textarea(attrs={'rows': 6}),
        }
        labels = {
          'title': 'Titre',
        }


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
