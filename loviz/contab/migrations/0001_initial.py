# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'contab_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('ruc', self.gf('django.db.models.fields.CharField')(max_length=11)),
        ))
        db.send_create_signal(u'contab', ['Cliente'])

        # Adding model 'Cuenta_Cliente'
        db.create_table(u'contab_cuenta_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contab.Cliente'])),
            ('deuda', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('abono', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'contab', ['Cuenta_Cliente'])

        # Adding model 'MaterialUsado'
        db.create_table(u'contab_materialusado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contab.Material'])),
            ('modelo_calzado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contab.Cliente'])),
            ('usado_en', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('price_docena', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'contab', ['MaterialUsado'])

        # Adding model 'Material'
        db.create_table(u'contab_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('cantidad_compra', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unidad_compra', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'contab', ['Material'])

        # Adding model 'Firme'
        db.create_table(u'contab_firme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('talla', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'contab', ['Firme'])

        # Adding model 'Modelos_calzado'
        db.create_table(u'contab_modelos_calzado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('costo', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'contab', ['Modelos_calzado'])

        # Adding model 'Venta'
        db.create_table(u'contab_venta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contab.Cliente'])),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contab.Modelos_calzado'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unidada_venta', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('precio_unidad', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'contab', ['Venta'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'contab_cliente')

        # Deleting model 'Cuenta_Cliente'
        db.delete_table(u'contab_cuenta_cliente')

        # Deleting model 'MaterialUsado'
        db.delete_table(u'contab_materialusado')

        # Deleting model 'Material'
        db.delete_table(u'contab_material')

        # Deleting model 'Firme'
        db.delete_table(u'contab_firme')

        # Deleting model 'Modelos_calzado'
        db.delete_table(u'contab_modelos_calzado')

        # Deleting model 'Venta'
        db.delete_table(u'contab_venta')


    models = {
        u'contab.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruc': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        u'contab.cuenta_cliente': {
            'Meta': {'object_name': 'Cuenta_Cliente'},
            'abono': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contab.Cliente']"}),
            'deuda': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'contab.firme': {
            'Meta': {'object_name': 'Firme'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'talla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'contab.material': {
            'Meta': {'object_name': 'Material'},
            'cantidad_compra': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'unidad_compra': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'contab.materialusado': {
            'Meta': {'object_name': 'MaterialUsado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contab.Material']"}),
            'modelo_calzado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contab.Cliente']"}),
            'price_docena': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'usado_en': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'contab.modelos_calzado': {
            'Meta': {'object_name': 'Modelos_calzado'},
            'costo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'contab.venta': {
            'Meta': {'object_name': 'Venta'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contab.Cliente']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contab.Modelos_calzado']"}),
            'precio_unidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unidada_venta': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['contab']