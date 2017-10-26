from django.views.generic import DetailView, ListView

from .models import Destination


class DestinationListView(ListView):
    model = Destination


class DestinationDetailView(DetailView):
    model = Destination
