# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Reporter'
        db.create_table('showTimeReport_reporter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('udid', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('showTimeReport', ['Reporter'])

        # Adding model 'WrongShowtime'
        db.create_table('showTimeReport_wrongshowtime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movieName', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('theaterName', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('showtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('receiveTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('showTimeReport', ['WrongShowtime'])


    def backwards(self, orm):
        
        # Deleting model 'Reporter'
        db.delete_table('showTimeReport_reporter')

        # Deleting model 'WrongShowtime'
        db.delete_table('showTimeReport_wrongshowtime')


    models = {
        'showTimeReport.reporter': {
            'Meta': {'object_name': 'Reporter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'udid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'showTimeReport.wrongshowtime': {
            'Meta': {'object_name': 'WrongShowtime'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movieName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'receiveTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'showtime': ('django.db.models.fields.DateTimeField', [], {}),
            'theaterName': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['showTimeReport']
