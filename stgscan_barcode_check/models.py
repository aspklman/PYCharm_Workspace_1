from django.db import models

# Create your models here.
class Outboxd(models.Model):
    fact_no = models.CharField(primary_key=True,max_length=4)
    outbox_no = models.CharField(primary_key=True,max_length=12)

    class Meta:
        db_table = 'outboxd'

class Stgscan_rec(models.Model):
    fact_no = models.CharField(primary_key=True,max_length=4)
    bar_no = models.CharField(primary_key=True,max_length=12)

    class Meta:
        db_table = 'stgscan_rec'

class Stgscan_barcode_check(models.Model):
    fact_no = models.CharField(primary_key=True,max_length=4)
    cont_no = models.CharField(primary_key=True,max_length=12)
    bar_no = models.CharField(primary_key=True, max_length=64)

    class Meta:
        db_table = 'stgscan_barcode_check_bak'

class Odrsscc_pp_xml(models.Model):
    marknumberfrom = models.CharField(primary_key=True,max_length=64)

    class Meta:
        db_table = 'odrsscc_pp_xml'

class V_sis_sis_barcode_check_f(models.Model):
    fact_no = models.CharField(primary_key=True,max_length=4)
    ctn_no = models.CharField(primary_key=True,max_length=12)
    sku_number = models.CharField(max_length=64)
    qty = models.IntegerField()

    class Meta:
        db_table = 'v_sis_sis_barcode_check_f'

class V_sis_sis_barcode_check_c(models.Model):
    fact_no = models.CharField(primary_key=True,max_length=4)
    ctn_no = models.CharField(primary_key=True,max_length=20)
    sku_number = models.CharField(max_length=64)
    qty = models.IntegerField()

    class Meta:
        db_table = 'v_sis_sis_barcode_check_c'