from django.conf.urls import url

from .views import DestinationDetailView, DestinationListView

urlpatterns = [
    url(r'^$', DestinationListView.as_view(), name='destination_list'),
    url(r'^(?P<slug>[^/]+)/$', DestinationDetailView.as_view(), name='destination_detail'),
]
