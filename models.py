# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TalcherDirect(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    pgma = models.TextField(db_column='PGMA', blank=True, null=True)  # Field name made lowercase.
    system = models.TextField(db_column='System', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talcher direct'
