from django.db import models


class Supplier(models.Model):
    updtick_0 = models.IntegerField(db_column='UPDTICK_0')
    supplier = models.CharField(db_column='BPSNUM_0', unique=True, max_length=15)
    company_name = models.CharField(db_column='BPSNAM_0', max_length=35)
    short_description = models.CharField(db_column='BPSSHO_0', max_length=10)
    supplier_type = models.SmallIntegerField(db_column='BPSTYP_0')
    category = models.CharField(db_column='BSGCOD_0', max_length=5)
    pay_to = models.CharField(db_column='BPRPAY_0', max_length=15)
    pay_to_address = models.CharField(db_column='BPAPAY_0', max_length=5)
    supplier_invoice = models.CharField(db_column='BPSINV_0', max_length=15)
    billing_address = models.CharField(db_column='BPAINV_0', max_length=5)
    supplier_group = models.CharField(db_column='BPSGRU_0', max_length=15)
    risk_supplier = models.CharField(db_column='BPSRSK_0', max_length=15)
    customer_number = models.CharField(db_column='BPCNUMBPS_0', max_length=15)
    carrier = models.CharField(db_column='BPTNUM_0', max_length=15)
    default_contact = models.CharField(db_column='CNTNAM_0', max_length=35)
    location = models.CharField(db_column='LOC_0', max_length=10)
    abc_class = models.SmallIntegerField(db_column='ABCCLS_0')
    unavailable = models.CharField(db_column='UVYCOD_0', max_length=5)
    currency = models.CharField(db_column='CUR_0', max_length=3)
    rate_type = models.SmallIntegerField(db_column='CHGTYP_0')
    payment_term = models.CharField(db_column='PTE_0', max_length=15)
    discount_code = models.CharField(db_column='DEP_0', max_length=5)
    tax_rule = models.CharField(db_column='VACBPR_0', max_length=5)
    delivery_mode = models.CharField(db_column='MDL_0', max_length=5)
    incoterm = models.CharField(db_column='EECICT_0', max_length=5)
    intrastat_transport_location = models.SmallIntegerField(db_column='EECLOC_0')
    statistical_group_0 = models.CharField(db_column='TSSCOD_0', max_length=20)
    statistical_group_1 = models.CharField(db_column='TSSCOD_1', max_length=20)
    statistical_group_2 = models.CharField(db_column='TSSCOD_2', max_length=20)
    statistical_group_3 = models.CharField(db_column='TSSCOD_3', max_length=20)
    statistical_group_4 = models.CharField(db_column='TSSCOD_4', max_length=20)
    invoice_amount_0 = models.DecimalField(db_column='INVDTAAMT_0', max_digits=20, decimal_places=5)
    invoice_amount_1 = models.DecimalField(db_column='INVDTAAMT_1', max_digits=20, decimal_places=5)
    invoice_amount_2 = models.DecimalField(db_column='INVDTAAMT_2', max_digits=20, decimal_places=5)
    invoice_amount_3 = models.DecimalField(db_column='INVDTAAMT_3', max_digits=20, decimal_places=5)
    invoice_amount_4 = models.DecimalField(db_column='INVDTAAMT_4', max_digits=20, decimal_places=5)
    invoice_amount_5 = models.DecimalField(db_column='INVDTAAMT_5', max_digits=20, decimal_places=5)
    invoice_amount_6 = models.DecimalField(db_column='INVDTAAMT_6', max_digits=20, decimal_places=5)
    invoice_amount_7 = models.DecimalField(db_column='INVDTAAMT_7', max_digits=20, decimal_places=5)
    invoice_amount_8 = models.DecimalField(db_column='INVDTAAMT_8', max_digits=20, decimal_places=5)
    invoice_amount_9 = models.DecimalField(db_column='INVDTAAMT_9', max_digits=20, decimal_places=5)
    invoice_amount_10 = models.DecimalField(db_column='INVDTAAMT_10', max_digits=20, decimal_places=5)
    invoice_amount_11 = models.DecimalField(db_column='INVDTAAMT_11', max_digits=20, decimal_places=5)
    invoice_amount_12 = models.DecimalField(db_column='INVDTAAMT_12', max_digits=20, decimal_places=5)
    invoice_amount_13 = models.DecimalField(db_column='INVDTAAMT_13', max_digits=20, decimal_places=5)
    invoice_amount_14 = models.DecimalField(db_column='INVDTAAMT_14', max_digits=20, decimal_places=5)
    invoice_amount_15 = models.DecimalField(db_column='INVDTAAMT_15', max_digits=20, decimal_places=5)
    invoice_amount_16 = models.DecimalField(db_column='INVDTAAMT_16', max_digits=20, decimal_places=5)
    invoice_amount_17 = models.DecimalField(db_column='INVDTAAMT_17', max_digits=20, decimal_places=5)
    invoice_amount_18 = models.DecimalField(db_column='INVDTAAMT_18', max_digits=20, decimal_places=5)
    invoice_amount_19 = models.DecimalField(db_column='INVDTAAMT_19', max_digits=20, decimal_places=5)
    invoice_amount_20 = models.DecimalField(db_column='INVDTAAMT_20', max_digits=20, decimal_places=5)
    invoice_amount_21 = models.DecimalField(db_column='INVDTAAMT_21', max_digits=20, decimal_places=5)
    invoice_amount_22 = models.DecimalField(db_column='INVDTAAMT_22', max_digits=20, decimal_places=5)
    invoice_amount_23 = models.DecimalField(db_column='INVDTAAMT_23', max_digits=20, decimal_places=5)
    invoice_amount_24 = models.DecimalField(db_column='INVDTAAMT_24', max_digits=20, decimal_places=5)
    invoice_amount_25 = models.DecimalField(db_column='INVDTAAMT_25', max_digits=20, decimal_places=5)
    invoice_amount_26 = models.DecimalField(db_column='INVDTAAMT_26', max_digits=20, decimal_places=5)
    invoice_amount_27 = models.DecimalField(db_column='INVDTAAMT_27', max_digits=20, decimal_places=5)
    invoice_amount_28 = models.DecimalField(db_column='INVDTAAMT_28', max_digits=20, decimal_places=5)
    invoice_amount_29 = models.DecimalField(db_column='INVDTAAMT_29', max_digits=20, decimal_places=5)
    invoicing_element_0 = models.SmallIntegerField(db_column='INVDTA_0')
    invoicing_element_1 = models.SmallIntegerField(db_column='INVDTA_1')
    invoicing_element_2 = models.SmallIntegerField(db_column='INVDTA_2')
    invoicing_element_3 = models.SmallIntegerField(db_column='INVDTA_3')
    invoicing_element_4 = models.SmallIntegerField(db_column='INVDTA_4')
    invoicing_element_5 = models.SmallIntegerField(db_column='INVDTA_5')
    invoicing_element_6 = models.SmallIntegerField(db_column='INVDTA_6')
    invoicing_element_7 = models.SmallIntegerField(db_column='INVDTA_7')
    invoicing_element_8 = models.SmallIntegerField(db_column='INVDTA_8')
    invoicing_element_9 = models.SmallIntegerField(db_column='INVDTA_9')
    invoicing_element_10 = models.SmallIntegerField(db_column='INVDTA_10')
    invoicing_element_11 = models.SmallIntegerField(db_column='INVDTA_11')
    invoicing_element_12 = models.SmallIntegerField(db_column='INVDTA_12')
    invoicing_element_13 = models.SmallIntegerField(db_column='INVDTA_13')
    invoicing_element_14 = models.SmallIntegerField(db_column='INVDTA_14')
    invoicing_element_15 = models.SmallIntegerField(db_column='INVDTA_15')
    invoicing_element_16 = models.SmallIntegerField(db_column='INVDTA_16')
    invoicing_element_17 = models.SmallIntegerField(db_column='INVDTA_17')
    invoicing_element_18 = models.SmallIntegerField(db_column='INVDTA_18')
    invoicing_element_19 = models.SmallIntegerField(db_column='INVDTA_19')
    invoicing_element_20 = models.SmallIntegerField(db_column='INVDTA_20')
    invoicing_element_21 = models.SmallIntegerField(db_column='INVDTA_21')
    invoicing_element_22 = models.SmallIntegerField(db_column='INVDTA_22')
    invoicing_element_23 = models.SmallIntegerField(db_column='INVDTA_23')
    invoicing_element_24 = models.SmallIntegerField(db_column='INVDTA_24')
    invoicing_element_25 = models.SmallIntegerField(db_column='INVDTA_25')
    invoicing_element_26 = models.SmallIntegerField(db_column='INVDTA_26')
    invoicing_element_27 = models.SmallIntegerField(db_column='INVDTA_27')
    invoicing_element_28 = models.SmallIntegerField(db_column='INVDTA_28')
    invoicing_element_29 = models.SmallIntegerField(db_column='INVDTA_29')
    amount_code_0 = models.SmallIntegerField(db_column='AMTCOD_0')
    amount_code_1 = models.SmallIntegerField(db_column='AMTCOD_1')
    amount_code_2 = models.SmallIntegerField(db_column='AMTCOD_2')
    amount_code_3 = models.SmallIntegerField(db_column='AMTCOD_3')
    amount_code_4 = models.SmallIntegerField(db_column='AMTCOD_4')
    amount_code_5 = models.SmallIntegerField(db_column='AMTCOD_5')
    amount_code_6 = models.SmallIntegerField(db_column='AMTCOD_6')
    amount_code_7 = models.SmallIntegerField(db_column='AMTCOD_7')
    amount_code_8 = models.SmallIntegerField(db_column='AMTCOD_8')
    amount_code_9 = models.SmallIntegerField(db_column='AMTCOD_9')
    amount_code_10 = models.SmallIntegerField(db_column='AMTCOD_10')
    amount_code_11 = models.SmallIntegerField(db_column='AMTCOD_11')
    amount_code_12 = models.SmallIntegerField(db_column='AMTCOD_12')
    amount_code_13 = models.SmallIntegerField(db_column='AMTCOD_13')
    amount_code_14 = models.SmallIntegerField(db_column='AMTCOD_14')
    amount_code_15 = models.SmallIntegerField(db_column='AMTCOD_15')
    amount_code_16 = models.SmallIntegerField(db_column='AMTCOD_16')
    amount_code_17 = models.SmallIntegerField(db_column='AMTCOD_17')
    amount_code_18 = models.SmallIntegerField(db_column='AMTCOD_18')
    amount_code_19 = models.SmallIntegerField(db_column='AMTCOD_19')
    amount_code_20 = models.SmallIntegerField(db_column='AMTCOD_20')
    amount_code_21 = models.SmallIntegerField(db_column='AMTCOD_21')
    amount_code_22 = models.SmallIntegerField(db_column='AMTCOD_22')
    amount_code_23 = models.SmallIntegerField(db_column='AMTCOD_23')
    amount_code_24 = models.SmallIntegerField(db_column='AMTCOD_24')
    amount_code_25 = models.SmallIntegerField(db_column='AMTCOD_25')
    amount_code_26 = models.SmallIntegerField(db_column='AMTCOD_26')
    amount_code_27 = models.SmallIntegerField(db_column='AMTCOD_27')
    amount_code_28 = models.SmallIntegerField(db_column='AMTCOD_28')
    amount_code_29 = models.SmallIntegerField(db_column='AMTCOD_29')
    price_list_structure = models.CharField(db_column='PLISTC_0', max_length=10)
    payment_bank = models.CharField(db_column='PAYBAN_0', max_length=5)
    accounting_code = models.CharField(db_column='ACCCOD_0', max_length=10)
    dimension_type_code_0 = models.CharField(db_column='DIE_0', max_length=3)
    dimension_type_code_1 = models.CharField(db_column='DIE_1', max_length=3)
    dimension_type_code_2 = models.CharField(db_column='DIE_2', max_length=3)
    dimension_type_code_3 = models.CharField(db_column='DIE_3', max_length=3)
    dimension_type_code_4 = models.CharField(db_column='DIE_4', max_length=3)
    dimension_type_code_5 = models.CharField(db_column='DIE_5', max_length=3)
    dimension_type_code_6 = models.CharField(db_column='DIE_6', max_length=3)
    dimension_type_code_7 = models.CharField(db_column='DIE_7', max_length=3)
    dimension_type_code_8 = models.CharField(db_column='DIE_8', max_length=3)
    dimension_type_code_9 = models.CharField(db_column='DIE_9', max_length=3)
    dimension_type_code_10 = models.CharField(db_column='DIE_10', max_length=3)
    dimension_type_code_11 = models.CharField(db_column='DIE_11', max_length=3)
    dimension_type_code_12 = models.CharField(db_column='DIE_12', max_length=3)
    dimension_type_code_13 = models.CharField(db_column='DIE_13', max_length=3)
    dimension_type_code_14 = models.CharField(db_column='DIE_14', max_length=3)
    dimension_type_code_15 = models.CharField(db_column='DIE_15', max_length=3)
    dimension_type_code_16 = models.CharField(db_column='DIE_16', max_length=3)
    dimension_type_code_17 = models.CharField(db_column='DIE_17', max_length=3)
    dimension_type_code_18 = models.CharField(db_column='DIE_18', max_length=3)
    dimension_type_code_19 = models.CharField(db_column='DIE_19', max_length=3)
    dimension_0 = models.CharField(db_column='CCE_0', max_length=15)
    dimension_1 = models.CharField(db_column='CCE_1', max_length=15)
    dimension_2 = models.CharField(db_column='CCE_2', max_length=15)
    dimension_3 = models.CharField(db_column='CCE_3', max_length=15)
    dimension_4 = models.CharField(db_column='CCE_4', max_length=15)
    dimension_5 = models.CharField(db_column='CCE_5', max_length=15)
    dimension_6 = models.CharField(db_column='CCE_6', max_length=15)
    dimension_7 = models.CharField(db_column='CCE_7', max_length=15)
    dimension_8 = models.CharField(db_column='CCE_8', max_length=15)
    dimension_9 = models.CharField(db_column='CCE_9', max_length=15)
    dimension_10 = models.CharField(db_column='CCE_10', max_length=15)
    dimension_11 = models.CharField(db_column='CCE_11', max_length=15)
    dimension_12 = models.CharField(db_column='CCE_12', max_length=15)
    dimension_13 = models.CharField(db_column='CCE_13', max_length=15)
    dimension_14 = models.CharField(db_column='CCE_14', max_length=15)
    dimension_15 = models.CharField(db_column='CCE_15', max_length=15)
    dimension_16 = models.CharField(db_column='CCE_16', max_length=15)
    dimension_17 = models.CharField(db_column='CCE_17', max_length=15)
    dimension_18 = models.CharField(db_column='CCE_18', max_length=15)
    dimension_19 = models.CharField(db_column='CCE_19', max_length=15)
    default_address = models.CharField(db_column='BPAADD_0', max_length=5)
    multi_line_order = models.SmallIntegerField(db_column='SEVLIN_0')
    order_text = models.CharField(db_column='ORDTEX_0', max_length=17)
    return_text = models.CharField(db_column='RTNTEX_0', max_length=17)
    lead_time_ranking_coefficient = models.DecimalField(db_column='LTIMRKCOE_0', max_digits=18, decimal_places=7)
    price_ranking_coefficient = models.DecimalField(db_column='PRIMRKCOE_0', max_digits=18, decimal_places=7)
    quality_ranking_coefficient = models.DecimalField(db_column='QLYMRKCOE_0', max_digits=18, decimal_places=7)
    quantity_ranking_coefficient = models.DecimalField(db_column='QTYMRKCOE_0', max_digits=18, decimal_places=7)
    free_ranking_coefficient = models.DecimalField(db_column='RSKMRKCOE_0', max_digits=18, decimal_places=7)
    lead_time_ranking = models.DecimalField(db_column='LTIMRK_0', max_digits=7, decimal_places=3)
    price_ranking = models.DecimalField(db_column='PRIMRK_0', max_digits=7, decimal_places=3)
    quality_ranking = models.DecimalField(db_column='QLYMRK_0', max_digits=7, decimal_places=3)
    quantity_ranking = models.DecimalField(db_column='QTYMRK_0', max_digits=7, decimal_places=3)
    free_ranking = models.DecimalField(db_column='RSKMRK_0', max_digits=7, decimal_places=3)
    total_ranking = models.DecimalField(db_column='GENMRK_0', max_digits=8, decimal_places=3)
    minimum_order_amount = models.DecimalField(db_column='ORDMINAMT_0', max_digits=27, decimal_places=13)
    credit_control = models.SmallIntegerField(db_column='OSTCTL_0')
    authorized_credit = models.DecimalField(db_column='OSTAUZAMT_0', max_digits=27, decimal_places=13)
    intrastat_statistical_increase = models.DecimalField(db_column='EECINCRAT_0', max_digits=8, decimal_places=3)
    notes = models.CharField(db_column='BPSREM_0', max_length=250)
    due_date_origin = models.SmallIntegerField(db_column='DUDCLC_0')
    currency_rate_determination = models.SmallIntegerField(db_column='CURCLC_0')
    must_remind_delivery = models.SmallIntegerField(db_column='FUPFLG_0')
    must_remind_acknowledgment = models.SmallIntegerField(db_column='OCNFLG_0')
    is_das_2_submitted = models.SmallIntegerField(db_column='DADFLG_0')
    service_supplier_code = models.CharField(db_column='PRVNUM_0', max_length=1)
    dispute_status = models.SmallIntegerField(db_column='DOUFLG_0')
    is_active = models.SmallIntegerField(db_column='ENAFLG_0')
    is_payment_held = models.SmallIntegerField(db_column='PAYLOKFLG_0')
    must_print_order_form = models.SmallIntegerField(db_column='NORPRNFLG_0')
    must_print_receipt_note = models.SmallIntegerField(db_column='NREPRNFLG_0')
    must_print_return_slip = models.SmallIntegerField(db_column='NRTPRNFLG_0')
    withholding_code = models.CharField(db_column='RITCOD_0', max_length=1)
    number_of_codes = models.SmallIntegerField(db_column='RITNBR_0')
    withholding_tax_allowance = models.DecimalField(db_column='RITRAT_0', max_digits=28, decimal_places=8)
    number_of_partners = models.SmallIntegerField(db_column='RITPARNBR_0')
    name_of_partner = models.CharField(db_column='RITPARNAM_0', max_length=1)
    partner_held = models.DecimalField(db_column='RITPARCOE_0', max_digits=28, decimal_places=8)
    cai_number = models.CharField(db_column='CAI_0', max_length=1)
    cai_validity_date = models.DateTimeField(db_column='DATVLYCAI_0')
    vat_collection_agent = models.SmallIntegerField(db_column='AGTPCP_0')
    regional_taxes = models.SmallIntegerField(db_column='AGTSATTAX_0')
    provinces = models.CharField(db_column='SATTAX_0', max_length=1)
    collection_agent = models.SmallIntegerField(db_column='FLGSATTAX_0')
    customer_number_for_supplier = models.CharField(db_column='BPCNUM_0', max_length=1)
    template_code = models.CharField(db_column='TPMCOD_0', max_length=5)
    account_structure = models.CharField(db_column='DIA_0', max_length=10)
    expense_allocation = models.CharField(db_column='IPTEXS_0', max_length=20)
    export_number = models.IntegerField(db_column='EXPNUM_0')
    create_user = models.CharField(db_column='CREUSR_0', max_length=5)
    create_date = models.DateTimeField(db_column='CREDAT_0')
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5)
    update_date = models.DateTimeField(db_column='UPDDAT_0')
    matching_tolerance = models.CharField(db_column='MATTOL_0', max_length=5)
    form_1099 = models.SmallIntegerField(db_column='FRM1099_0')
    box_1099 = models.CharField(db_column='BOX1099_0', max_length=1)
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0')
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0')
    auuid = models.BinaryField(db_column='AUUID_0')
    is_281_submitted = models.SmallIntegerField(db_column='FLG281_0')
    amount_type = models.SmallIntegerField(db_column='PURPRITYP_0')
    is_cash_vat = models.SmallIntegerField(db_column='CSHVAT_0')
    cash_vat_deadline = models.DateTimeField(db_column='CSHDAT_0')
    auto_invoice_code = models.CharField(db_column='AUTINVCOD_0', max_length=5)
    free_freight_threshold = models.DecimalField(db_column='ORDFREFRT_0', max_digits=27, decimal_places=13)
    payroll_interface_distribution = models.CharField(db_column='BPRDSP_0', max_length=10)
    rex_number = models.CharField(db_column='REXNUM_0', max_length=30)
    has_no_whit_list_verification = models.SmallIntegerField(db_column='WLFLG_0')
    zeditor_0 = models.SmallIntegerField(db_column='ZEDITOR_0')
    default_invoicing_module = models.SmallIntegerField(db_column='INVORIMOD_0')
    id = models.BigAutoField(db_column='ROWID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'BPSUPPLIER'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
