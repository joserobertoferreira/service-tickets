from django.db import models
from django.utils import timezone


class CodeNumbers(models.Model):
    id = models.BigAutoField(db_column='ROWID', primary_key=True)
    sequence_number = models.CharField(db_column='CODNUM_0', unique=True, max_length=5)
    length = models.SmallIntegerField(db_column='LNG_0', default=0)
    definition_level = models.SmallIntegerField(db_column='NIVDEF_0', default=1)
    rtz_level = models.SmallIntegerField(db_column='NIVRAZ_0', default=1)
    type = models.SmallIntegerField(db_column='TYP_0', default=1)
    number_of_components = models.SmallIntegerField(db_column='NBPOS_0', default=1)
    component_type_0 = models.SmallIntegerField(db_column='POSTYP_0', default=1)
    component_type_1 = models.SmallIntegerField(db_column='POSTYP_1', default=1)
    component_type_2 = models.SmallIntegerField(db_column='POSTYP_2', default=1)
    component_type_3 = models.SmallIntegerField(db_column='POSTYP_3', default=1)
    component_type_4 = models.SmallIntegerField(db_column='POSTYP_4', default=1)
    component_type_5 = models.SmallIntegerField(db_column='POSTYP_5', default=1)
    component_type_6 = models.SmallIntegerField(db_column='POSTYP_6', default=1)
    component_type_7 = models.SmallIntegerField(db_column='POSTYP_7', default=1)
    component_type_8 = models.SmallIntegerField(db_column='POSTYP_8', default=1)
    component_type_9 = models.SmallIntegerField(db_column='POSTYP_9', default=1)
    component_length_0 = models.SmallIntegerField(db_column='POSLNG_0', default=0)
    component_length_1 = models.SmallIntegerField(db_column='POSLNG_1', default=0)
    component_length_2 = models.SmallIntegerField(db_column='POSLNG_2', default=0)
    component_length_3 = models.SmallIntegerField(db_column='POSLNG_3', default=0)
    component_length_4 = models.SmallIntegerField(db_column='POSLNG_4', default=0)
    component_length_5 = models.SmallIntegerField(db_column='POSLNG_5', default=0)
    component_length_6 = models.SmallIntegerField(db_column='POSLNG_6', default=0)
    component_length_7 = models.SmallIntegerField(db_column='POSLNG_7', default=0)
    component_length_8 = models.SmallIntegerField(db_column='POSLNG_8', default=0)
    component_length_9 = models.SmallIntegerField(db_column='POSLNG_9', default=0)
    constants_0 = models.CharField(db_column='POSCTE_0', max_length=80, default='')
    constants_1 = models.CharField(db_column='POSCTE_1', max_length=80, default='')
    constants_2 = models.CharField(db_column='POSCTE_2', max_length=80, default='')
    constants_3 = models.CharField(db_column='POSCTE_3', max_length=80, default='')
    constants_4 = models.CharField(db_column='POSCTE_4', max_length=80, default='')
    constants_5 = models.CharField(db_column='POSCTE_5', max_length=80, default='')
    constants_6 = models.CharField(db_column='POSCTE_6', max_length=80, default='')
    constants_7 = models.CharField(db_column='POSCTE_7', max_length=80, default='')
    constants_8 = models.CharField(db_column='POSCTE_8', max_length=80, default='')
    constants_9 = models.CharField(db_column='POSCTE_9', max_length=80, default='')
    crono_control = models.SmallIntegerField(db_column='CTLCHR_0', default=0)
    reset_to_zero = models.SmallIntegerField(db_column='ZERO_0', default=1)
    sequence = models.SmallIntegerField(db_column='SEQ_0', default=1)
    table = models.CharField(db_column='SEQTBL_0', max_length=12, default='')
    abbreviation = models.CharField(db_column='SEQABR_0', max_length=8, default='')
    numerals = models.SmallIntegerField(db_column='SEQNBR_0', default=0)
    legislation = models.CharField(db_column='LEG_0', max_length=20, default='')
    create_user = models.CharField(db_column='CREUSR_0', max_length=5, default='INTER')
    create_date = models.DateTimeField(db_column='CREDAT_0', default=timezone.now)
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5, default='INTER')
    update_date = models.DateTimeField(db_column='UPDDAT_0', default=timezone.now)
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0', auto_now_add=True)
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0', auto_now=True)

    updtick = models.IntegerField(db_column='UPDTICK_0', default=1)
    auuid = models.BinaryField(db_column='AUUID_0')

    class Meta:
        managed = False
        db_table = 'ACODNUM'


class SequenceNumbers(models.Model):
    id = models.BigAutoField(db_column='ROWID', primary_key=True)
    sequence_number = models.CharField(db_column='CODNUM_0', unique=True, max_length=5)
    site = models.CharField(db_column='SITE_0', max_length=5, default='')
    period = models.SmallIntegerField(db_column='PERIODE_0', default=0)
    complement = models.CharField(db_column='COMP_0', max_length=25, default='')
    value = models.DecimalField(db_column='VALEUR_0', max_digits=21, decimal_places=1, default=0)
    create_user = models.CharField(db_column='CREUSR_0', max_length=5, default='INTER')
    update_user = models.CharField(db_column='UPDUSR_0', max_length=5, default='INTER')
    create_datetime = models.DateTimeField(db_column='CREDATTIM_0', auto_now_add=True)
    update_datetime = models.DateTimeField(db_column='UPDDATTIM_0', auto_now=True)

    updtick = models.IntegerField(db_column='UPDTICK_0', default=1)
    auuid = models.BinaryField(db_column='AUUID_0')

    class Meta:
        managed = False
        db_table = 'AVALNUM'
        unique_together = (('sequence_number', 'site', 'period', 'complement'),)
