from django.contrib import admin

from tickets.models import Ticket

admin.site.register(Ticket)
# @admin.register(Ticket)
# class TicketAdmin(admin.ModelAdmin):
#     list_display = ('service_number', 'ticket_date', 'customer', 'title')
#     search_fields = ('title', 'description')
#     list_filter = ('created_at', 'updated_at')
#     ordering = ('-created_at',)
