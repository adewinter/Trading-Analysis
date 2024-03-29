# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'MarketDataPoint.InstrumentName'
        db.alter_column('financials_marketdatapoint', 'InstrumentName', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.High'
        db.alter_column('financials_marketdatapoint', 'High', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.Volume'
        db.alter_column('financials_marketdatapoint', 'Volume', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.Low'
        db.alter_column('financials_marketdatapoint', 'Low', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.PercentageChange'
        db.alter_column('financials_marketdatapoint', 'PercentageChange', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.Close'
        db.alter_column('financials_marketdatapoint', 'Close', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.AfrikaansInstrumentName'
        db.alter_column('financials_marketdatapoint', 'AfrikaansInstrumentName', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.Open'
        db.alter_column('financials_marketdatapoint', 'Open', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.InstrumentIdentifier'
        db.alter_column('financials_marketdatapoint', 'InstrumentIdentifier', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.Change'
        db.alter_column('financials_marketdatapoint', 'Change', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MarketDataPoint.Movement'
        db.alter_column('financials_marketdatapoint', 'Movement', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'MarketDataPoint.InstrumentName'
        db.alter_column('financials_marketdatapoint', 'InstrumentName', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.High'
        db.alter_column('financials_marketdatapoint', 'High', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.Volume'
        db.alter_column('financials_marketdatapoint', 'Volume', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.Low'
        db.alter_column('financials_marketdatapoint', 'Low', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.PercentageChange'
        db.alter_column('financials_marketdatapoint', 'PercentageChange', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.Close'
        db.alter_column('financials_marketdatapoint', 'Close', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.AfrikaansInstrumentName'
        db.alter_column('financials_marketdatapoint', 'AfrikaansInstrumentName', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.Open'
        db.alter_column('financials_marketdatapoint', 'Open', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.InstrumentIdentifier'
        db.alter_column('financials_marketdatapoint', 'InstrumentIdentifier', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.Change'
        db.alter_column('financials_marketdatapoint', 'Change', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MarketDataPoint.Movement'
        db.alter_column('financials_marketdatapoint', 'Movement', self.gf('django.db.models.fields.CharField')(default='', max_length=100))


    models = {
        'financials.company': {
            'Meta': {'object_name': 'Company'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ticker_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'financials.marketdatapoint': {
            'AfrikaansInstrumentName': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Change': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Close': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'High': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'InstrumentIdentifier': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'InstrumentName': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Low': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'MarketDataPoint'},
            'Movement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Open': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'PercentageChange': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Volume': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
