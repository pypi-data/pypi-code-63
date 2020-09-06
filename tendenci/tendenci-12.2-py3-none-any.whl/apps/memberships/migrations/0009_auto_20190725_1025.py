# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-25 10:25


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0008_auto_20180315_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipappfield',
            name='field_type',
            field=models.CharField(blank=True, choices=[('', 'Set to Default'), ('CharField', 'Text'), ('CharField/django.forms.Textarea', 'Paragraph Text'), ('BooleanField', 'Checkbox'), ('ChoiceField', 'Select One (Drop Down)'), ('ChoiceField/django.forms.RadioSelect', 'Select One (Radio Buttons)'), ('MultipleChoiceField', 'Multi select (Drop Down)'), ('MultipleChoiceField/django.forms.CheckboxSelectMultiple', 'Multi select (Checkboxes)'), ('CountrySelectField', 'Countries Drop Down'), ('EmailField', 'Email'), ('FileField', 'File upload'), ('DateField/django.forms.widgets.SelectDateWidget', 'Date'), ('DateTimeField', 'Date/time'), ('section_break', 'Section Break')], max_length=64, verbose_name='Field Type'),
        ),
    ]
