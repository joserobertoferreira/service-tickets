# Generated by Django 5.0.13 on 2025-04-05 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'managed': False, 'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
    ]
