# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Reporter(models.Model):
    udid = models.CharField(max_length=255)

    def __unicode__(self):
        return self.udid
    class Admin:
        pass
        
class WrongShowtime(models.Model):
    movieName = models.CharField(max_length=32)
    theaterName = models.CharField(max_length=32)
    showtime = models.DateTimeField()
    receiveTime = models.DateTimeField(auto_now=True)
    #test = models.CharField(max_length=32)
    def __unicode__(self):
        return "%s, %s, %s" %(self.theaterName, self.movieName, self.showtime)
    
    class Admin:
        pass