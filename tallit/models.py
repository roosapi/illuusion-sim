from django.db import models

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


class Owner(models.Model):
    vrl = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=65)
    url = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'owner'


class Horse(models.Model):
    name = models.CharField(max_length=45)
    status = models.PositiveIntegerField()
    breed = models.CharField(max_length=45)
    sex = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=225, blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    colour = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    sire = models.ForeignKey('self', models.DO_NOTHING, db_column='sire', blank=True, null=True, related_name="horse_sire")
    dam = models.ForeignKey('self', models.DO_NOTHING, db_column='dam', blank=True, null=True,related_name="horse_dam")
    pedigree = models.CharField(max_length=45, blank=True, null=True)
    evm = models.IntegerField()
    vh = models.CharField(max_length=45, blank=True, null=True)
    owner = models.CharField(max_length=15, blank=True, null=True)
    stable = models.CharField(max_length=45, blank=True, null=True)
    breeder = models.ForeignKey(Breeder, models.DO_NOTHING, db_column='breeder', blank=True, null=True)
    discipline = models.CharField(max_length=45, blank=True, null=True)
    level = models.CharField(max_length=45, blank=True, null=True)
    shows = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horse'

    def __str__(self):
        return self.name


class Competition(models.Model):
    horse = models.ForeignKey('Horse', models.DO_NOTHING)
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
        unique_together = (('horse', 'discipline', 'date', 'location', 'url', 'class_field', 'result', 'participants'),)


class Copyright(models.Model):
    name = models.CharField(unique=True, max_length=45)
    url = models.CharField(max_length=145, blank=True, null=True)
    license = models.CharField(max_length=45, blank=True, null=True)
    license_url = models.CharField(max_length=145, blank=True, null=True)
    info = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copyright'

class HorseImg(models.Model):
    horse = models.ForeignKey(Horse, models.DO_NOTHING, db_column='horse')
    name = models.CharField(max_length=140)
    copy = models.ForeignKey(Copyright, models.DO_NOTHING, db_column='copy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horse_img'


class HorseText(models.Model):
    horse = models.ForeignKey(Horse, models.DO_NOTHING, related_name='horsetext')
    date = models.DateField()
    title = models.CharField(max_length=250)
    text = models.TextField()
    copy = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'horse_text'
        unique_together = (('horse', 'date', 'title'),)


class Merit(models.Model):
    horse = models.ForeignKey(Horse, models.DO_NOTHING, related_name='merit')
    merit = models.CharField(max_length=10)
    event = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField()
    url = models.CharField(max_length=65)
    info = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merit'

class Show(models.Model):
    type = models.CharField(max_length=3)
    horse = models.ForeignKey(Horse, models.DO_NOTHING)
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
        unique_together = (('horse', 'url', 'class_field'),)
