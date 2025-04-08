from django.db import models
from django.utils import timezone


class Address(models.Model):
    id = models.BigAutoField(db_column='ROWID', primary_key=True)
    entity_type = models.SmallIntegerField(db_column='BPATYP_0')
    entity_number = models.CharField(db_column='BPANUM_0', max_length=15, default='')
    code = models.CharField(db_column='BPAADD_0', max_length=5, default='')
    description = models.CharField(db_column='BPADES_0', max_length=30, default='')
    default_bank_id = models.CharField(db_column='BPABID_0', max_length=30, default='')
    is_default = models.SmallIntegerField(db_column='BPAADDFLG_0', default=1)
    address_line_0 = models.CharField(db_column='BPAADDLIG_0', max_length=50, default='')
    address_line_1 = models.CharField(db_column='BPAADDLIG_1', max_length=50, default='')
    address_line_2 = models.CharField(db_column='BPAADDLIG_2', max_length=50, default='')
    postal_code = models.CharField(db_column='POSCOD_0', max_length=10, default='')
    city = models.CharField(db_column='CTY_0', max_length=40, default='')
    federal_id_code = models.CharField(db_column='CODSEE_0', max_length=1, default='')
    state = models.CharField(db_column='SAT_0', max_length=35, default='')
    country = models.CharField(db_column='CRY_0', max_length=3, default='')
    country_name = models.CharField(db_column='CRYNAM_0', max_length=40, default='')
    telephone_0 = models.CharField(db_column='TEL_0', max_length=40, default='')
    telephone_1 = models.CharField(db_column='TEL_1', max_length=40, default='')
    telephone_2 = models.CharField(db_column='TEL_2', max_length=40, default='')
    telephone_3 = models.CharField(db_column='TEL_3', max_length=40, default='')
    telephone_4 = models.CharField(db_column='TEL_4', max_length=40, default='')
    fax = models.CharField(db_column='FAX_0', max_length=40, default='')
    mobile_phone = models.CharField(db_column='MOB_0', max_length=40, default='')
    email_address_0 = models.CharField(db_column='WEB_0', max_length=80, default='')
    email_address_1 = models.CharField(db_column='WEB_1', max_length=80, default='')
    email_address_2 = models.CharField(db_column='WEB_2', max_length=80, default='')
    email_address_3 = models.CharField(db_column='WEB_3', max_length=80, default='')
    email_address_4 = models.CharField(db_column='WEB_4', max_length=80, default='')
    website = models.CharField(db_column='FCYWEB_0', max_length=250, default='')
    external_id = models.CharField(db_column='EXTNUM_0', max_length=30, default='')
    is_valid = models.SmallIntegerField(db_column='ADRVAL_0', default=1)
    gln = models.CharField(db_column='GLNCOD_0', max_length=13, default='')
    site_tax_id = models.CharField(db_column='CRN_0', max_length=20, default='')

    export_number = models.IntegerField(db_column='EXPNUM_0', default=0)
    create_user = models.CharField(db_column='CREUSR_0', max_length=5, default='INTER')
    create_date = models.DateTimeField(db_column='CREDAT_0', default=timezone.now)
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5, default='INTER')
    update_date = models.DateTimeField(db_column='UPDDAT_0', default=timezone.now)
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0', auto_now_add=True)
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0', auto_now=True)
    auuid = models.BinaryField(db_column='AUUID_0')
    updtick = models.IntegerField(db_column='UPDTICK_0', default=1)

    class Meta:
        managed = False
        db_table = 'BPADDRESS'
        unique_together = (('entity_type', 'entity_number', 'code'),)
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
