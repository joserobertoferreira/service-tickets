from django.db import models
from django.utils import timezone


class Relationship(models.Model):
    id = models.BigAutoField(db_column='ROWID', primary_key=True)
    code = models.CharField(db_column='CNTNUM_0', unique=True, max_length=15)
    full_name = models.CharField(db_column='CNTFULNAM_0', max_length=60)
    last_name = models.CharField(db_column='CNTLNA_0', max_length=35)
    first_name = models.CharField(db_column='CNTFNA_0', max_length=20)
    email = models.EmailField(db_column='CNTEMA_0', max_length=80, unique=True, default='')
    title = models.SmallIntegerField(db_column='CNTTTL_0', default=1)
    type = models.SmallIntegerField(db_column='CNTTYP_0', default=1)
    date_of_birth = models.DateTimeField(db_column='CNTBIR_0', null=False, blank=True)
    language = models.CharField(db_column='CNTLAN_0', max_length=3, default='POR')
    professional_category = models.CharField(db_column='CNTCSP_0', max_length=20, default='')
    country = models.CharField(db_column='CRY_0', max_length=3, default='')
    country_name = models.CharField(db_column='CRYNAM_0', max_length=40, default='')
    address_0 = models.CharField(db_column='ADD_0', max_length=50, default='')
    address_1 = models.CharField(db_column='ADD_1', max_length=50, default='')
    address_2 = models.CharField(db_column='ADD_2', max_length=50, default='')
    postal_code = models.CharField(db_column='ZIP_0', max_length=10, default='')
    city = models.CharField(db_column='CTY_0', max_length=40, default='')
    state = models.CharField(db_column='SAT_0', max_length=35, default='')
    landline = models.CharField(db_column='CNTETS_0', max_length=40, default='')
    fax = models.CharField(db_column='CNTFAX_0', max_length=40, default='')
    cell_phone = models.CharField(db_column='CNTMOB_0', max_length=40, default='')
    is_mailing_prohibited = models.SmallIntegerField(db_column='CNTFBDMAG_0', default=1)
    create_user = models.CharField(db_column='CREUSR_0', max_length=5, default='INTER')
    create_date = models.DateTimeField(db_column='CREDAT_0', default=timezone.now)
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5, default='INTER')
    update_date = models.DateTimeField(db_column='UPDDAT_0', default=timezone.now)
    export_number = models.IntegerField(db_column='EXPNUM_0', default=0)
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0', auto_now_add=True)
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0', auto_now=True)
    auuid = models.BinaryField(db_column='AUUID_0')
    identity_card = models.CharField(db_column='UIDCRDNUM_0', max_length=1, default='')
    social_security_fund = models.DecimalField(db_column='SSCNUM_0', max_digits=28, decimal_places=8, default=0)
    visa = models.CharField(db_column='RDEPITNUM_0', max_length=1, default='')

    class Meta:
        managed = False
        db_table = 'CONTACTCRM'
        unique_together = (('type', 'code'), ('email', 'code'))
        verbose_name = 'Relationship'
        verbose_name_plural = 'Relationships'

    def __str__(self):
        return self.code


class Contact(models.Model):
    id = models.BigAutoField(db_column='ROWID', primary_key=True)
    entity_type = models.SmallIntegerField(db_column='BPATYP_0', default=1)
    partner = models.CharField(db_column='BPANUM_0', max_length=15)
    contact_relationship = models.CharField(db_column='CCNCRM_0', max_length=15)
    address_code = models.CharField(db_column='BPAADD_0', max_length=5, default='')
    email = models.CharField(db_column='WEB_0', max_length=80, default='')

    updtick_0 = models.IntegerField(db_column='UPDTICK_0', default=1)
    position = models.SmallIntegerField(db_column='CNTFNC_0', default=1)
    department = models.CharField(db_column='CNTSRV_0', max_length=30, default='')
    role = models.CharField(db_column='CNTMSS_0', max_length=20, default='')
    phone = models.CharField(db_column='TEL_0', max_length=40, default='')
    fax = models.CharField(db_column='FAX_0', max_length=40, default='')
    mobile = models.CharField(db_column='MOB_0', max_length=40, default='')
    data_protection = models.SmallIntegerField(db_column='DPO_0', default=1)
    create_user = models.CharField(db_column='CREUSR_0', max_length=5, default='INTER')
    create_date = models.DateTimeField(db_column='CREDAT_0', default=timezone.now)
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5, default='INTER')
    update_date = models.DateTimeField(db_column='UPDDAT_0', default=timezone.now)
    export_number = models.IntegerField(db_column='EXPNUM_0', default=0)
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0', auto_now_add=True)
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0', auto_now=True)
    auuid = models.BinaryField(db_column='AUUID_0')

    class Meta:
        managed = False
        db_table = 'CONTACT'
        unique_together = (
            ('entity_type', 'partner', 'contact_relationship'),
            ('contact_relationship', 'entity_type', 'partner'),
        )
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.contact_relationship
