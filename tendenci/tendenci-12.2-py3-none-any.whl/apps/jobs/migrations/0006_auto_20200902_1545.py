# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20190816_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='job',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='jobpricing',
            name='creator_username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='jobpricing',
            name='owner_username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
