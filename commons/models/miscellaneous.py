from django.db import models


class TicketStatus(models.Model):
    language = models.CharField(db_column='LANGUE_0', max_length=3, verbose_name='Language')
    code = models.CharField(db_column='IDENT2_0', max_length=80, verbose_name='Code')
    description = models.CharField(db_column='TEXTE_0', max_length=80, verbose_name='Description')

    class Meta:
        managed = False
        db_table = 'YSRESTA'


class TicketSeverity(models.Model):
    language = models.CharField(db_column='LANGUE_0', max_length=3, verbose_name='Language')
    code = models.CharField(db_column='IDENT2_0', max_length=80, verbose_name='Code')
    description = models.CharField(db_column='TEXTE_0', max_length=80, verbose_name='Description')

    class Meta:
        managed = False
        db_table = 'YSREGRALEV'


class TicketPriority(models.Model):
    language = models.CharField(db_column='LANGUE_0', max_length=3, verbose_name='Language')
    code = models.CharField(db_column='IDENT2_0', max_length=80, verbose_name='Code')
    description = models.CharField(db_column='TEXTE_0', max_length=80, verbose_name='Description')

    class Meta:
        managed = False
        db_table = 'YSREPIOLEV'
