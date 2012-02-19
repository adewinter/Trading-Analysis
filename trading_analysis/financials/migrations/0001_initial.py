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

        # Adding model 'MarketDataPoint'
        db.create_table('financials_marketdatapoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financials.Company'])),
            ('AfrikaansInstrumentName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Change', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Close', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('High', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('InstrumentIdentifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('InstrumentName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Low', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Movement', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Open', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('PercentageChange', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Volume', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('financials', ['MarketDataPoint'])


    def backwards(self, orm):
        
        # Deleting model 'Company'
        db.delete_table('financials_company')

        # Deleting model 'StatementItem'
        db.delete_table('financials_statementitem')

        # Deleting model 'MarketDataPoint'
        db.delete_table('financials_marketdatapoint')


    models = {
        'financials.company': {
            'Meta': {'object_name': 'Company'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ticker_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'financials.marketdatapoint': {
            'AfrikaansInstrumentName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Change': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Close': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'High': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'InstrumentIdentifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'InstrumentName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Low': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'MarketDataPoint'},
            'Movement': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Open': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'PercentageChange': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Volume': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financials.Company']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
