# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Data(models.Model):
    season = models.CharField(db_column='Season', max_length=3)  # Field name made lowercase.
    no_in_series = models.CharField(db_column='No_in_series', max_length=3)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=50)  # Field name made lowercase.
    deal = models.CharField(db_column='Deal', max_length=3)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=100)  # Field name made lowercase.
    entrepreneur_gender = models.CharField(db_column='Entrepreneur_Gender', max_length=10)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=10)  # Field name made lowercase.
    equity = models.CharField(db_column='Equity', max_length=4)  # Field name made lowercase.
    valuation = models.CharField(db_column='Valuation', max_length=10)  # Field name made lowercase.
    corcoran = models.CharField(db_column='Corcoran', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cuban = models.CharField(db_column='Cuban', max_length=2, blank=True, null=True)  # Field name made lowercase.
    griener = models.CharField(db_column='Griener', max_length=2, blank=True, null=True)  # Field name made lowercase.
    herjavec = models.CharField(db_column='Herjavec', max_length=2, blank=True, null=True)  # Field name made lowercase.
    john = models.CharField(db_column='John', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oleary = models.CharField(db_column='Oleary', max_length=2, blank=True, null=True)  # Field name made lowercase.
    harrington = models.CharField(db_column='Harrington', max_length=2, blank=True, null=True)  # Field name made lowercase.
    guest = models.CharField(db_column='Guest', max_length=2, blank=True, null=True)  # Field name made lowercase.
    no_of_sharks = models.CharField(db_column='No_of_sharks', max_length=2)  # Field name made lowercase.
    dollars_per_shark = models.CharField(db_column='Dollars_per_shark', max_length=10)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data'


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
