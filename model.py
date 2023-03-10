# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Engdjango(models.Model):
    ∩_sn = models.TextField(db_column='∩╗┐sn', blank=True, null=True)  # Field renamed to remove unsuitable characters.
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


class TalcherDirect(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    pgma = models.TextField(db_column='PGMA', blank=True, null=True)  # Field name made lowercase.
    system = models.TextField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    mu = models.TextField(db_column='MU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talcher direct'
