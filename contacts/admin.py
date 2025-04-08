from django.contrib import admin

from contacts.models import Relationship


@admin.register(Relationship)
class RelationshipUserAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'email')
    ordering = ('code',)
