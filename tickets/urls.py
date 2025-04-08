from django.urls import path

from tickets.views import TicketListView, page_not_found_view

app_name = 'tickets'
urlpatterns = [
    path('list/', TicketListView.as_view(), name='ticket_list'),
    path('not-found/', page_not_found_view, name='page_not_found'),
]
