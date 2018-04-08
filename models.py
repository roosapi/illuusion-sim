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


class Breed(models.Model):
    breed = models.CharField(primary_key=True, max_length=25)
    abbr = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'breed'
        unique_together = (('breed', 'abbr'),)


class Breeder(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)
    url = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breeder'


class Competition(models.Model):
    horse_id = models.IntegerField(primary_key=True)
    discipline = models.CharField(max_length=15)
    date = models.DateField()
    location = models.CharField(max_length=50)
    url = models.CharField(max_length=65)
    class_field = models.CharField(db_column='class', max_length=50)  # Field renamed because it was a Python reserved word.
    result = models.IntegerField()
    participants = models.IntegerField()
    winnings = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competition'
        unique_together = (('horse_id', 'discipline', 'date', 'location', 'url', 'class_field', 'result', 'participants'),)


class Copyright(models.Model):
    name = models.CharField(unique=True, max_length=45)
    url = models.CharField(max_length=145, blank=True, null=True)
    license = models.CharField(max_length=45, blank=True, null=True)
    license_url = models.CharField(max_length=145, blank=True, null=True)
    info = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copyright'


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


class Horse(models.Model):
    name = models.CharField(max_length=45)
    status = models.IntegerField()
    breed = models.CharField(max_length=45)
    sex = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=225, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    colour = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    sire = models.IntegerField(blank=True, null=True)
    dam = models.IntegerField(blank=True, null=True)
    pedigree = models.CharField(max_length=45, blank=True, null=True)
    evm = models.IntegerField()
    vh = models.CharField(max_length=45, blank=True, null=True)
    owner = models.CharField(max_length=25, blank=True, null=True)
    stable = models.CharField(max_length=45, blank=True, null=True)
    breeder = models.IntegerField(blank=True, null=True)
    discipline = models.CharField(max_length=45, blank=True, null=True)
    level = models.CharField(max_length=45, blank=True, null=True)
    shows = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horse'


class HorseImg(models.Model):
    horse = models.IntegerField()
    name = models.CharField(max_length=140)
    copy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horse_img'


class HorseText(models.Model):
    horse_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=250)
    text = models.TextField()
    copy = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'horse_text'
        unique_together = (('horse_id', 'date', 'title'),)


class Merit(models.Model):
    horse_id = models.IntegerField()
    merit = models.CharField(max_length=10)
    event = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField()
    url = models.CharField(max_length=65)
    info = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merit'


class Owner(models.Model):
    vrl = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=65)
    url = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'owner'


class Show(models.Model):
    type = models.CharField(max_length=3)
    horse_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    location = models.CharField(max_length=65)
    url = models.CharField(max_length=65)
    class_field = models.CharField(db_column='class', max_length=65)  # Field renamed because it was a Python reserved word.
    result = models.CharField(max_length=10)
    evaluation = models.CharField(max_length=10, blank=True, null=True)
    judge = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'show'
        unique_together = (('horse_id', 'url', 'class_field'),)
