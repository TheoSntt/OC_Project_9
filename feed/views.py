from itertools import chain

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from reviews.models import Review



@login_required
def feed(request):
    tickets = Ticket.objects.all()
    reviews= Review.objects.all()
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    return render(request, 'feed/feed.html',
    {'tickets_and_reviews': tickets_and_reviews})
