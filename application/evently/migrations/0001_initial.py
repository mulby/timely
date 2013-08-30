# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Source'
        db.create_table(u'evently_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'evently', ['Source'])

        # Adding model 'Event'
        db.create_table(u'evently_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evently.Source'])),
        ))
        db.send_create_signal(u'evently', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Source'
        db.delete_table(u'evently_source')

        # Deleting model 'Event'
        db.delete_table(u'evently_event')


    models = {
        u'evently.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['evently.Source']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'evently.source': {
            'Meta': {'object_name': 'Source'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['evently']