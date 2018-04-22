from django.db import models

class Omistaja(models.Model):
    vrl = models.CharField(primary_key=True, max_length=15)
    nimi = models.CharField(max_length=65)
    url = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'omistaja'


class Rotu(models.Model):
    rotu = models.CharField(primary_key=True, max_length=25)
    rotu_lyh = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'rotu'
        unique_together = (('rotu', 'rotu_lyh'),)

class Hevonen(models.Model):
    nimi = models.CharField(max_length=65)
    osoite = models.CharField(max_length=225, blank=True, null=True)
    lempinimi = models.CharField(max_length=65, blank=True, null=True)
    vh_tunnus = models.CharField(max_length=65, blank=True, null=True)
    rotu = models.CharField(max_length=65)
    skp = models.CharField(max_length=5)
    syntaika = models.DateField(blank=True, null=True)
    vari = models.CharField(max_length=65, blank=True, null=True)
    saka = models.IntegerField(blank=True, null=True)
    omistaja = models.ForeignKey('Omistaja', models.DO_NOTHING, db_column='omistaja', blank=True, null=True)
    kasvattaja = models.CharField(max_length=65, blank=True, null=True)
    kasvattaja_url = models.CharField(max_length=225, blank=True, null=True)
    painotus = models.CharField(max_length=25, blank=True, null=True)
    koulutustaso = models.CharField(max_length=40, blank=True, null=True)
    nayttelyt = models.IntegerField(blank=True, null=True)
    luonne = models.TextField(blank=True, null=True)
    isa = models.ForeignKey('self', models.DO_NOTHING, db_column='isa', blank=True, null=True)
    ema = models.ForeignKey('self', models.DO_NOTHING, db_column='ema', blank=True, null=True)
    suku = models.IntegerField()
    evm = models.IntegerField()
    status = models.CharField(max_length=25, blank=True, null=True)
    talli = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hevonen'
        unique_together = (('nimi', 'rotu', 'skp', 'syntaika'),)


class HevonenKuva(models.Model):
    hevonen = models.ForeignKey(Hevonen, models.DO_NOTHING, db_column='hevonen')
    thumb = models.CharField(max_length=150)
    kuva_url = models.CharField(max_length=225)
    kuvaaja = models.CharField(max_length=65)
    kuvaaja_url = models.CharField(max_length=150, blank=True, null=True)
    lisatiedot = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hevonen_kuva'


class HevonenTekstit(models.Model):
    hevonen = models.ForeignKey(Hevonen, models.DO_NOTHING, primary_key=True)
    pvm = models.DateField()
    otsikko = models.CharField(max_length=250)
    teksti = models.TextField()
    kirjoittaja = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'hevonen_tekstit'
        unique_together = (('hevonen', 'pvm', 'otsikko'),)


class Meriitit(models.Model):
    hevonen = models.ForeignKey(Hevonen, models.DO_NOTHING)
    saavutus = models.CharField(max_length=10)
    tilaisuus = models.CharField(max_length=150, blank=True, null=True)
    pvm = models.DateField()
    url = models.CharField(max_length=65)
    info = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meriitit'


class MuuKisa(models.Model):
    hevonen = models.ForeignKey(Hevonen, models.DO_NOTHING, primary_key=True)
    laji = models.CharField(max_length=15)
    pvm = models.DateField()
    paikka = models.CharField(max_length=50)
    kutsu_url = models.CharField(max_length=65)
    luokka = models.CharField(max_length=50)
    sija = models.IntegerField()
    osallistujia = models.IntegerField()
    voittosumma = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'muu_kisa'
        unique_together = (('hevonen', 'laji', 'pvm', 'paikka', 'kutsu_url', 'luokka', 'sija', 'osallistujia'),)


class Nayttelyt(models.Model):
    jaos = models.CharField(max_length=3)
    hevonen = models.ForeignKey(Hevonen, models.DO_NOTHING, primary_key=True)
    pvm = models.DateField()
    paikka = models.CharField(max_length=65)
    kutsu_url = models.CharField(max_length=65)
    luokka = models.CharField(max_length=65)
    sija = models.CharField(max_length=10)
    tulos = models.CharField(max_length=10, blank=True, null=True)
    tuomari = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'nayttelyt'
        unique_together = (('hevonen', 'kutsu_url', 'luokka'),)



