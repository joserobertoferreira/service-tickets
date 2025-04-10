from customers.models import Partner


def common_data(request):
    """
    Context processor to add common data to the context.
    """
    company_name = None

    if request.user.is_authenticated:
        partner = Partner.objects.filter(european_vat_number=request.user.vat_number).first()

        if partner:
            company_name = partner.company_name_0
        else:
            company_name = request.user.vat_number

    return {
        'company_name': company_name,
    }
