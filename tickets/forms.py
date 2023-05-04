from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from tickets.models import Ticket

class TicketForm(forms.ModelForm):
   edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
   class Meta:
     model = Ticket
     fields = ['title', 'description', 'image']

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)