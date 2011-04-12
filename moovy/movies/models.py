# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Publisher(models.Model):
    chtName        = models.CharField(max_length=64)
    enName         = models.CharField(max_length=64)
    url            = models.URLField()

    def __unicode__(self):
        return self.chtName
class MovieDetail(models.Model):
    pass

class MoviePhoto(models.Model):
    thumbnailUrl   = models.URLField()
    smallUrl       = models.URLField()
    imageUrl       = models.URLField()
    movie          = models.ForeignKey(MovieDetail)

    def __unicode__(self):
        return self.imageUrl

class Person(models.Model):
    chtName     = models.CharField(max_length=64)
    enName      = models.CharField(max_length=64)
    movieBefore = models.CharField(max_length=64)
    def __unicode__(self):
        return self.chtName

class MovieDetail(models.Model):
    intro       = models.TextField()
    url         = models.URLField()
    director    = models.ForeignKey(Person)
    casts       = models.ManyToManyField(Person)
    poster      = models.ForeignKey(MoviePhoto,unique=True)
    
    def __unicode__(self):
        return self.chtName

class Movie(models.Model):
    chtName     = models.CharField(max_length=64)
    enName      = models.CharField(max_length=64)
    mClass      = models.IntegerField()
    date        = models.DateField()
    length      = models.IntegerField()
    publisher   = models.ForeignKey(Publisher)

    def __unicode__(self):
        return self.chtName

class MovieAlias(models.Model):
    chtName     = models.CharField(max_length=64)
    movie       = models.ForeignKey(Movie)

    def __unicode__(self):
        return self.chtName

class Area(models.Model):
    id      = models.IntegerField(primary_key=True)
    chtName = models.CharField(max_length=10)
    enName  = models.CharField(max_length=10)
    def __unicode__(self):
        return self.chtName
class Theater(models.Model):
    id   = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    tel  = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    lat  = models.FloatField()
    lng  = models.FloatField()
    area = models.ForeignKey(Area)
    url  = models.URLField()
    showtimeUrl = models.URLField()
    iconUrl = models.URLField()
    iconUrl2 = models.URLField()

    def __unicode__(self):
        return self.name

class Showtime(models.Model):
    LANG = (
        (u'',u''),
        (u'國語',u'國語發音'),
        (u'英語',u'英語發音'),
        (u'日語',u'日語發音'),
        (u'粵語',u'粵語發音'),
    )

    showtime = models.DateTimeField()
    digital  = models.BooleanField()
    threeD   = models.BooleanField()
    imax     = models.BooleanField()
    other    = models.CharField(max_length=10)
    lang     = models.CharField(max_length=10,choices=LANG)
    roomName = models.CharField(max_length=10)
    booklink = models.URLField()

    def genType(self):
        type = u''
        type += self.other
        if self.digital : type += u'數位'
        if self.threeD  : type += u'3D'
        if self.imax    : type += u'IMAX'
        type += self.lang
        return type

    def __unicode__(self):
        return u'%s %s' % (unicode(self.showtime),self.genType)