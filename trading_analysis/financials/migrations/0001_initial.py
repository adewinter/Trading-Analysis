# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Company'
        db.create_table('financials_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ticker_symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('financials', ['Company'])

        # Adding model 'StatementItem'
        db.create_table('financials_statementitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financials.Company'])),
        ))
        db.send_create_signal('financials', ['StatementItem'])


    def backwards(self, orm):
        
        # Deleting model 'Company'
        db.delete_table('financials_company')

        # Deleting model 'StatementItem'
        db.delete_table('financials_statementitem')


    models = {
        'financials.company': {
            'Meta': {'object_name': 'Company'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ticker_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'financials.statementitem': {
            'Meta': {'object_name': 'StatementItem'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financials.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['financials']
