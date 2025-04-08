from django.shortcuts import render

from customers.models import Partner


def search_customer_by_nif(request):
    search_nif = request.GET.get('vat_number', '')

    customer_name = ''

    try:
        search_nif = search_nif.upper()
        customer = Partner.objects.filter(european_vat_number=search_nif).first()

        if customer:
            customer_name = customer.company_name_0

    except Partner.DoesNotExist:
        pass

    context = {'customer_name': customer_name}

    return render(request, 'accounts/partials/search_customer.html', context)
