import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from contacts.models import Contact, Relationship
from customers.models import Address, Partner

User = get_user_model()

# Alias do banco de dados legado definido em settings.py se estiver usando 2 bancos diferentes
# LEGACY_DB_ALIAS = 'legacy'


@receiver(post_save, sender=User)
def create_user_contact(sender, instance, created, **kwargs):
    """
    Create a user profile when a new user is created.
    """
    uuid_bytes = uuid.uuid4().bytes

    user_data = {
        'contact_code': instance.username,
        'first_name': instance.first_name,
        'last_name': instance.last_name,
        'email': instance.email,
        'vat_number': instance.vat_number,
        'full_name': f'{instance.first_name.upper()}\\{instance.last_name.upper()}',
    }

    # Select the business partner information for user instance
    partners_data = Partner.objects.filter(european_vat_number=user_data['vat_number']).first()

    if partners_data is None:
        print(f'Nenhum parceiro encontrado para o usuário {user_data["contact_code"]}')
        return

    address_data = Address.objects.filter(entity_number=partners_data.bp, code=partners_data.default_address).first()

    if address_data is None:
        print(f'Nenhum endereço encontrado para o parceiro {partners_data.bp}')
        return

    try:
        # Try to create the contact relationship and the contact in x3 database

        relationship, created_in_legacy = Relationship.objects.get_or_create(
            defaults={
                'country': partners_data.country,
                'country_name': address_data.country_name,
                'date_of_birth': settings.DEFAULT_LEGACY_DATE,
                'auuid': uuid_bytes,
            },
            code=user_data['contact_code'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            full_name=user_data['full_name'],
        )

        if created_in_legacy:
            print(f'Registro criado na tabela CONTACTCRM {user_data["contact_code"]}')

            # If the relationship was created, create the contact
            contact, created_in_legacy = Contact.objects.get_or_create(
                defaults={
                    'auuid': uuid_bytes,
                },
                entity_type=1,
                partner=partners_data.bp,
                contact_relationship=user_data['contact_code'],
                address_code=partners_data.default_address,
                email=user_data['email'],
            )

            if created_in_legacy:
                print(f'Registro criado na tabela CONTACT {user_data["contact_code"]}')
            else:
                print(f'Registro já existente na tabela CONTACT {user_data["contact_code"]}')

        else:
            print(f'Registro já existente na tabela CONTACTCRM {user_data["contact_code"]}')

    except Exception as e:
        # É CRUCIAL tratar exceções aqui!
        # O que fazer se a inserção no DB legado falhar? Logar o erro?
        # Impedir a criação do User (difícil em post_save)? Enviar notificação?
        print(f'ERRO ao criar registro na tabela CONTACTCRM {user_data["contact_code"]}: {e}')
        # Considere usar o logging do Python/Django para registrar erros
        # import logging
        # logger = logging.getLogger(__name__)
        # logger.error(f"Falha ao criar contato legado para
        # user {instance.pk} (code={contact_code}): {e}", exc_info=True)
        pass  # Ou tome outra ação apropriada
