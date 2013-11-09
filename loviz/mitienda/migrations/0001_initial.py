# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calzado'
        db.create_table(u'mitienda_calzado', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['shop.Product'], unique=True, primary_key=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('descuento', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'mitienda', ['Calzado'])

        # Adding M2M table for field categorias on 'Calzado'
        m2m_table_name = db.shorten_name(u'mitienda_calzado_categorias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('calzado', models.ForeignKey(orm[u'mitienda.calzado'], null=False)),
            ('categoria', models.ForeignKey(orm[u'mitienda.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['calzado_id', 'categoria_id'])

        # Adding M2M table for field palabras_claves on 'Calzado'
        m2m_table_name = db.shorten_name(u'mitienda_calzado_palabras_claves')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('calzado', models.ForeignKey(orm[u'mitienda.calzado'], null=False)),
            ('palabrasclaves', models.ForeignKey(orm[u'mitienda.palabrasclaves'], null=False))
        ))
        db.create_unique(m2m_table_name, ['calzado_id', 'palabrasclaves_id'])

        # Adding model 'Categoria'
        db.create_table(u'mitienda_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('peso', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('relacion_padre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mitienda.Categoria'], blank=True)),
        ))
        db.send_create_signal(u'mitienda', ['Categoria'])

        # Adding model 'PalabrasClaves'
        db.create_table(u'mitienda_palabrasclaves', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'mitienda', ['PalabrasClaves'])


    def backwards(self, orm):
        # Deleting model 'Calzado'
        db.delete_table(u'mitienda_calzado')

        # Removing M2M table for field categorias on 'Calzado'
        db.delete_table(db.shorten_name(u'mitienda_calzado_categorias'))

        # Removing M2M table for field palabras_claves on 'Calzado'
        db.delete_table(db.shorten_name(u'mitienda_calzado_palabras_claves'))

        # Deleting model 'Categoria'
        db.delete_table(u'mitienda_categoria')

        # Deleting model 'PalabrasClaves'
        db.delete_table(u'mitienda_palabrasclaves')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mitienda.calzado': {
            'Meta': {'object_name': 'Calzado', '_ormbases': ['shop.Product']},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mitienda.Categoria']", 'symmetrical': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'descuento': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'palabras_claves': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mitienda.PalabrasClaves']", 'symmetrical': 'False', 'blank': 'True'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'mitienda.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'peso': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'relacion_padre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mitienda.Categoria']", 'blank': 'True'})
        },
        u'mitienda.palabrasclaves': {
            'Meta': {'object_name': 'PalabrasClaves'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['mitienda']