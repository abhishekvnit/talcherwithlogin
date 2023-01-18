from django.db import models

# Create your models here.

from django.db import models


class TalcherDirect(models.Model):
    id = models.AutoField(db_column='ID', primary_key='True')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    pgma = models.TextField(db_column='PGMA', blank=True, null=True)  # Field name made lowercase.
    system = models.TextField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    mu = models.TextField(db_column='MU', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'talcher direct'


class Engdjango(models.Model):
    id = models.AutoField(db_column='ï»¿ID', primary_key='True')  # Field renamed to remove unsuitable characters.
    orgn_drg_no = models.TextField(db_column='ORGN DRG NO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    drg_title = models.TextField(db_column='DRG_TITLE', blank=True, null=True)  # Field name made lowercase.
    sub_system = models.TextField(db_column='SUB_SYSTEM', blank=True, null=True)  # Field name made lowercase.
    boi_name = models.TextField(db_column='BOI_NAME', blank=True, null=True)  # Field name made lowercase.
    sch_date = models.TextField(db_column='SCH_DATE', blank=True, null=True)  # Field name made lowercase.
    details = models.TextField(db_column='DETAILS', blank=True, null=True)  # Field name made lowercase.
    area = models.TextField(db_column='AREA', blank=True, null=True)  # Field name made lowercase.
    purpose = models.TextField(db_column='PURPOSE', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    appr_rvsn_no = models.TextField(db_column='APPR\nRVSN NO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    upload_dt = models.TextField(db_column='UPLOAD_DT', blank=True, null=True)  # Field name made lowercase.
    release_dt = models.TextField(db_column='RELEASE_DT', blank=True, null=True)  # Field name made lowercase.
    release_cat = models.TextField(db_column='RELEASE_CAT', blank=True, null=True)  # Field name made lowercase.
    category_id = models.TextField(db_column='CATEGORY ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mu = models.TextField(db_column='MU', blank=True, null=True)  # Field name made lowercase.
    due_sub = models.TextField(db_column='Due_sub', blank=True, null=True)  # Field name made lowercase.
    under_resubmission = models.TextField(db_column='Under_Resubmission', blank=True, null=True)  # Field name made lowercase.
    appr = models.TextField(db_column='Appr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'engdjango'