# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0002_auto_20180724_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
    ]
