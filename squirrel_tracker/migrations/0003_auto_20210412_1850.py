# Generated by Django 3.1.7 on 2021-04-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracker', '0002_auto_20210403_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='AboveGroundSighterMeasurement',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='AboveGroundSighterMeasurement'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(blank=True, null=True, verbose_name='Approaches'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(blank=True, null=True, verbose_name='Chasing'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(blank=True, null=True, verbose_name='Climbing'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='ColorNotes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ColorNotes'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='CombinationOfPrimaryAndHighlightColor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CombinationOfPrimaryAndHighlightColor'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Date',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(blank=True, null=True, verbose_name='Eating'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(blank=True, null=True, verbose_name='Foraging'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Hectare',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Hectare'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='HectareSquirrelNumber',
            field=models.IntegerField(blank=True, null=True, verbose_name='HectareSquirrelNumber'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='HighlightFurColor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='HighlightFurColor'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(blank=True, null=True, verbose_name='Indifferent'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(blank=True, null=True, verbose_name='Kuks'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='LatLong',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Latlong'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(blank=True, null=True, verbose_name='Moans'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='OtherActivities',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='OtherActivities'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='OtherInteractions',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='OtherInteractions'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='PrimaryFurColor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='PrimaryFurColor'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(blank=True, null=True, verbose_name='Quaas'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(blank=True, null=True, verbose_name='Running'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='RunsFrom',
            field=models.BooleanField(blank=True, null=True, verbose_name='RunsFrom'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Shift',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Shift'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='SpecificLocation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='SpecificLocation'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='TailFlags',
            field=models.BooleanField(blank=True, null=True, verbose_name='TailFlags'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='TailTwitches',
            field=models.BooleanField(blank=True, null=True, verbose_name='TailTwitches'),
        ),
    ]