# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50)),
                ('object_id', models.IntegerField(default=0, null=True, blank=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('creator_username', models.CharField(max_length=50, null=True)),
                ('owner_username', models.CharField(max_length=50, null=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('tender_date', models.DateTimeField(null=True)),
                ('arrival_date_time', models.DateTimeField(null=True, blank=True)),
                ('is_void', models.BooleanField(default=False)),
                ('status_detail', models.CharField(default='estimate', max_length=50, choices=[('estimate', 'Estimate'), ('tendered', 'Tendered')])),
                ('status', models.BooleanField(default=True)),
                ('payments_credits', models.DecimalField(default=0, max_digits=15, decimal_places=2, blank=True)),
                ('balance', models.DecimalField(default=0, max_digits=15, decimal_places=2, blank=True)),
                ('total', models.DecimalField(max_digits=15, decimal_places=2, blank=True)),
                ('discount_code', models.CharField(max_length=100, null=True, verbose_name='Discount Code', blank=True)),
                ('discount_amount', models.DecimalField(default=0, verbose_name='Discount Amount', max_digits=10, decimal_places=2)),
                ('variance', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('variance_notes', models.TextField(max_length=1000, null=True, blank=True)),
                ('receipt', models.BooleanField(default=False)),
                ('gift', models.BooleanField(default=False)),
                ('greeting', models.CharField(max_length=500, null=True, blank=True)),
                ('instructions', models.CharField(max_length=500, null=True, blank=True)),
                ('po', models.CharField(max_length=50, blank=True)),
                ('terms', models.CharField(max_length=50, blank=True)),
                ('disclaimer', models.CharField(max_length=150, null=True, blank=True)),
                ('admin_notes', models.TextField(null=True, blank=True)),
                ('fob', models.CharField(max_length=50, null=True, blank=True)),
                ('project', models.CharField(max_length=50, null=True, blank=True)),
                ('other', models.CharField(max_length=120, null=True, blank=True)),
                ('message', models.CharField(max_length=150, null=True, blank=True)),
                ('subtotal', models.DecimalField(max_digits=15, decimal_places=2, blank=True)),
                ('tax_exempt', models.BooleanField(default=True)),
                ('tax_exemptid', models.CharField(max_length=50, null=True, blank=True)),
                ('tax_rate', models.FloatField(default=0, blank=True)),
                ('taxable', models.BooleanField(default=False)),
                ('tax', models.DecimalField(default=0, max_digits=15, decimal_places=4)),
                ('bill_to', models.CharField(max_length=120, blank=True)),
                ('bill_to_first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('bill_to_last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('bill_to_company', models.CharField(max_length=100, null=True, blank=True)),
                ('bill_to_address', models.CharField(max_length=250, null=True, blank=True)),
                ('bill_to_city', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_to_state', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_to_zip_code', models.CharField(max_length=20, null=True, blank=True)),
                ('bill_to_country', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_to_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_to_fax', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_to_email', models.CharField(max_length=100, null=True, blank=True)),
                ('ship_to', models.CharField(max_length=120, blank=True)),
                ('ship_to_first_name', models.CharField(max_length=50, blank=True)),
                ('ship_to_last_name', models.CharField(max_length=50, blank=True)),
                ('ship_to_company', models.CharField(max_length=100, blank=True)),
                ('ship_to_address', models.CharField(max_length=250, blank=True)),
                ('ship_to_city', models.CharField(max_length=50, blank=True)),
                ('ship_to_state', models.CharField(max_length=50, blank=True)),
                ('ship_to_zip_code', models.CharField(max_length=20, blank=True)),
                ('ship_to_country', models.CharField(max_length=50, blank=True)),
                ('ship_to_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('ship_to_fax', models.CharField(max_length=50, null=True, blank=True)),
                ('ship_to_email', models.CharField(max_length=100, null=True, blank=True)),
                ('ship_to_address_type', models.CharField(max_length=50, null=True, blank=True)),
                ('ship_date', models.DateTimeField()),
                ('ship_via', models.CharField(max_length=50, blank=True)),
                ('shipping', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('shipping_surcharge', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('box_and_packing', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('creator', models.ForeignKey(related_name='invoice_creator', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('entity', models.ForeignKey(related_name='invoices', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='entities.Entity', null=True)),
                ('object_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True, on_delete=django.db.models.deletion.CASCADE)),
                ('owner', models.ForeignKey(related_name='invoice_owner', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
        ),
    ]
