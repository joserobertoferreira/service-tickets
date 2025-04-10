from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from core.utils.database.db_query import execute_query
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

        ticket_list = context.get('object_list')

        if ticket_list:
            status_values = set(t.ticket_status for t in ticket_list if t.ticket_status is not None)
            self._get_full_status_code(status_values, ticket_list)

        return context

    def _get_full_status_code(self, status_values, ticket_list):  # noqa: PLR6301
        """
        Retrieves the full status code from the legacy database.

        Args:
            status_code: The status code to look up.

        Returns:
            str: The full status code description.
        """
        status_map = {}

        if status_values:
            placeholders = ','.join(['%s'] * len(status_values))

            query = f'SELECT IDENT2_0,TEXTE_0 FROM dbo.YSRESTA WHERE LANGUE_0 = %s AND IDENT2_0 IN ({placeholders})'
            params = ['POR'] + list(status_values)
            result = execute_query('default', query, params)

            for row in result:
                status_map[row['IDENT2_0']] = row['TEXTE_0']

        for ticket in ticket_list:
            if ticket.ticket_status is not None:
                description = status_map.get(ticket.ticket_status, 'Unknown')
                ticket.ticket_status = f'{ticket.ticket_status} - {description}'
            else:
                ticket.ticket_status = 'Unknown'

    def _get_full_priority_code(self, priority_values, ticket_list):  # noqa: PLR6301
        """
        Retrieves the full priority code from the legacy database.

        Args:
            priority_values: The priority code to look up.

        Returns:
            str: The full priority code description.
        """
        priority_map = {}

        if priority_values:
            placeholders = ','.join(['%s'] * len(priority_values))

            query = f'SELECT IDENT2_0,TEXTE_0 FROM dbo.YSREPIOLEV WHERE LANGUE_0 = %s AND IDENT2_0 IN ({placeholders})'
            params = ['POR'] + list(priority_values)
            result = execute_query('default', query, params)

            for row in result:
                priority_map[row['IDENT2_0']] = row['TEXTE_0']

        for ticket in ticket_list:
            if ticket.ticket_priority is not None:
                description = priority_map.get(ticket.ticket_priority, 'Unknown')
                ticket.ticket_priority = f'{ticket.ticket_priority} - {description}'
            else:
                ticket.ticket_priority = 'Unknown'

    def _get_full_severity_code(self, severity_values, ticket_list):  # noqa: PLR6301
        """
        Retrieves the full severity code from the legacy database.

        Args:
            severity_values: The severity code to look up.

        Returns:
            str: The full severity code description.
        """
        severity_map = {}

        if severity_values:
            placeholders = ','.join(['%s'] * len(severity_values))

            query = f'SELECT IDENT2_0,TEXTE_0 FROM dbo.YSREGRALEV WHERE LANGUE_0 = %s AND IDENT2_0 IN ({placeholders})'
            params = ['POR'] + list(severity_values)
            result = execute_query('default', query, params)

            for row in result:
                severity_map[row['IDENT2_0']] = row['TEXTE_0']

        for ticket in ticket_list:
            if ticket.ticket_severity is not None:
                description = severity_map.get(ticket.ticket_severity, 'Unknown')
                ticket.ticket_severity = f'{ticket.ticket_severity} - {description}'
            else:
                ticket.ticket_severity = 'Unknown'

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
