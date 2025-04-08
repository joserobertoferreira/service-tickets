from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from tickets.models import Ticket


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Tickets'
        context['no_ticket_message'] = 'No tickets available.'

        field_labels = {}

        fields_to_display = ['service_number', 'ticket_date', 'ticket_status', 'title', 'resolution_date']

        for field_name in fields_to_display:
            field_object = self.model._meta.get_field(field_name)
            field_labels[field_name] = field_object.verbose_name

        context['field_labels'] = field_labels

        return context

    def get_queryset(self):
        return Ticket.objects.filter(relationship=self.request.user.username).order_by('-ticket_date')


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'tickets/ticket_create.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):  # noqa: PLR6301
        return reverse('tickets:ticket_list')


def page_not_found_view(request):
    return render(request, 'core/error_404.html')
