# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ref', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NibrsActivityType',
            fields=[
                ('activity_type_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('activity_type_code', models.CharField(blank=True, max_length=2, null=True)),
                ('activity_type_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_activity_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsAge',
            fields=[
                ('age_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('age_code', models.CharField(blank=True, max_length=2, null=True)),
                ('age_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_age',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsArrestee',
            fields=[
                ('arrestee_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('arrestee_seq_num', models.BigIntegerField(blank=True, null=True)),
                ('arrest_num', models.CharField(blank=True, max_length=12, null=True)),
                ('arrest_date', models.DateTimeField(blank=True, null=True)),
                ('multiple_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('age_num', models.SmallIntegerField(blank=True, null=True)),
                ('sex_code', models.CharField(blank=True, max_length=1, null=True)),
                ('resident_code', models.CharField(blank=True, max_length=1, null=True)),
                ('under_18_disposition_code', models.CharField(blank=True, max_length=1, null=True)),
                ('clearance_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('age_range_low_num', models.SmallIntegerField(blank=True, null=True)),
                ('age_range_high_num', models.SmallIntegerField(blank=True, null=True)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsAge')),
            ],
            options={
                'db_table': 'nibrs_arrestee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsArresteeWeapon',
            fields=[
                ('nibrs_arrestee_weapon_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('arrestee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsArrestee')),
            ],
            options={
                'db_table': 'nibrs_arrestee_weapon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsArrestType',
            fields=[
                ('arrest_type_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('arrest_type_code', models.CharField(blank=True, max_length=1, null=True)),
                ('arrest_type_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_arrest_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsAssignmentType',
            fields=[
                ('assignment_type_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('assignment_type_code', models.CharField(blank=True, max_length=1, null=True)),
                ('assignment_type_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_assignment_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsBiasList',
            fields=[
                ('bias_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('bias_code', models.CharField(blank=True, max_length=2, null=True)),
                ('bias_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_bias_list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsBiasMotivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bias', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsBiasList')),
            ],
            options={
                'db_table': 'nibrs_bias_motivation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsCircumstances',
            fields=[
                ('circumstances_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('circumstances_type', models.CharField(blank=True, max_length=1, null=True)),
                ('circumstances_code', models.SmallIntegerField(blank=True, null=True)),
                ('circumstances_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_circumstances',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsClearedExcept',
            fields=[
                ('cleared_except_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('cleared_except_code', models.CharField(blank=True, max_length=1, null=True)),
                ('cleared_except_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_cleared_except',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsCriminalAct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'nibrs_criminal_act',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsCriminalActType',
            fields=[
                ('criminal_act_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('criminal_act_code', models.CharField(blank=True, max_length=1, null=True)),
                ('criminal_act_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_criminal_act_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsDrugMeasureType',
            fields=[
                ('drug_measure_type_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('drug_measure_code', models.CharField(blank=True, max_length=2, null=True)),
                ('drug_measure_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_drug_measure_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsEds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddocname', models.CharField(blank=True, max_length=100, null=True)),
                ('data_year', models.SmallIntegerField(blank=True, null=True)),
                ('month_num', models.SmallIntegerField(blank=True, null=True)),
                ('relative_rec_num', models.IntegerField(blank=True, null=True)),
                ('segment_action_type', models.CharField(blank=True, max_length=1, null=True)),
                ('ori', models.CharField(blank=True, max_length=9, null=True)),
                ('incident_num', models.CharField(blank=True, max_length=12, null=True)),
                ('level', models.CharField(blank=True, max_length=1, null=True)),
                ('offense_code', models.CharField(blank=True, max_length=3, null=True)),
                ('person_seq_num', models.CharField(blank=True, max_length=3, null=True)),
                ('type_prop_loss', models.CharField(blank=True, max_length=1, null=True)),
                ('data_element_num', models.CharField(blank=True, max_length=3, null=True)),
                ('error_num', models.SmallIntegerField(blank=True, null=True)),
                ('data_field', models.CharField(blank=True, max_length=12, null=True)),
                ('error_msg', models.CharField(blank=True, max_length=79, null=True)),
                ('submission_ser_num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nibrs_eds',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsEthnicity',
            fields=[
                ('ethnicity_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('ethnicity_code', models.CharField(blank=True, max_length=1, null=True)),
                ('ethnicity_name', models.CharField(blank=True, max_length=100, null=True)),
                ('hc_flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'nibrs_ethnicity',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsGrpbArrest',
            fields=[
                ('grpb_arrest_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('arrest_num', models.CharField(blank=True, max_length=15, null=True)),
                ('arrest_date', models.DateTimeField(blank=True, null=True)),
                ('arrest_seq_num', models.SmallIntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=4, null=True)),
                ('arrest_type_id', models.SmallIntegerField(blank=True, null=True)),
                ('offense_type_id', models.BigIntegerField(blank=True, null=True)),
                ('sex_code', models.CharField(blank=True, max_length=1, null=True)),
                ('resident_code', models.CharField(blank=True, max_length=1, null=True)),
                ('under_18_disposition_code', models.CharField(blank=True, max_length=1, null=True)),
                ('age_num', models.SmallIntegerField(blank=True, null=True)),
                ('arrest_year', models.SmallIntegerField(blank=True, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('data_home', models.CharField(blank=True, max_length=1, null=True)),
                ('ddocname', models.CharField(blank=True, max_length=100, null=True)),
                ('did', models.BigIntegerField(blank=True, null=True)),
                ('age_range_low_num', models.SmallIntegerField(blank=True, null=True)),
                ('age_range_high_num', models.SmallIntegerField(blank=True, null=True)),
                ('age', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsAge')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ref.RefAgency')),
                ('ethnicity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsEthnicity')),
            ],
            options={
                'db_table': 'nibrs_grpb_arrest',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsGrpbArrestWeapon',
            fields=[
                ('nibrs_grpb_arrest_weapon_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('grpb_arrest', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsGrpbArrest')),
            ],
            options={
                'db_table': 'nibrs_grpb_arrest_weapon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsIncident',
            fields=[
                ('incident_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('incident_number', models.CharField(blank=True, max_length=15, null=True)),
                ('cargo_theft_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('submission_date', models.DateTimeField(blank=True, null=True)),
                ('incident_date', models.DateTimeField(blank=True, null=True)),
                ('report_date_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('incident_hour', models.SmallIntegerField(blank=True, null=True)),
                ('cleared_except_date', models.DateTimeField(blank=True, null=True)),
                ('incident_status', models.SmallIntegerField(blank=True, null=True)),
                ('data_home', models.CharField(blank=True, max_length=1, null=True)),
                ('ddocname', models.CharField(blank=True, max_length=100, null=True)),
                ('orig_format', models.CharField(blank=True, max_length=1, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('did', models.BigIntegerField(blank=True, null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ref.RefAgency')),
                ('cleared_except', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsClearedExcept')),
            ],
            options={
                'db_table': 'nibrs_incident',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsInjury',
            fields=[
                ('injury_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('injury_code', models.CharField(blank=True, max_length=1, null=True)),
                ('injury_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_injury',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsJustifiableForce',
            fields=[
                ('justifiable_force_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('justifiable_force_code', models.CharField(blank=True, max_length=1, null=True)),
                ('justifiable_force_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_justifiable_force',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsLocationType',
            fields=[
                ('location_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('location_code', models.CharField(blank=True, max_length=2, null=True)),
                ('location_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_location_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsMonth',
            fields=[
                ('nibrs_month_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('month_num', models.SmallIntegerField()),
                ('data_year', models.SmallIntegerField()),
                ('reported_status', models.CharField(blank=True, max_length=1, null=True)),
                ('report_date', models.DateTimeField(blank=True, null=True)),
                ('prepared_date', models.DateTimeField(blank=True, null=True)),
                ('update_flag', models.CharField(max_length=1)),
                ('orig_format', models.CharField(max_length=1)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('data_home', models.CharField(blank=True, max_length=1, null=True)),
                ('ddocname', models.CharField(blank=True, max_length=50, null=True)),
                ('did', models.BigIntegerField(blank=True, null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ref.RefAgency')),
            ],
            options={
                'db_table': 'nibrs_month',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsOffender',
            fields=[
                ('offender_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('offender_seq_num', models.SmallIntegerField(blank=True, null=True)),
                ('age_num', models.SmallIntegerField(blank=True, null=True)),
                ('sex_code', models.CharField(blank=True, max_length=1, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('age_range_low_num', models.SmallIntegerField(blank=True, null=True)),
                ('age_range_high_num', models.SmallIntegerField(blank=True, null=True)),
                ('age', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsAge')),
                ('ethnicity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsEthnicity')),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsIncident')),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ref.RefRace')),
            ],
            options={
                'db_table': 'nibrs_offender',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsOffense',
            fields=[
                ('offense_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('attempt_complete_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('num_premises_entered', models.SmallIntegerField(blank=True, null=True)),
                ('method_entry_code', models.CharField(blank=True, max_length=1, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsIncident')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsLocationType')),
            ],
            options={
                'db_table': 'nibrs_offense',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsOffenseType',
            fields=[
                ('offense_type_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('offense_code', models.CharField(blank=True, max_length=5, null=True)),
                ('offense_name', models.CharField(blank=True, max_length=100, null=True)),
                ('crime_against', models.CharField(blank=True, max_length=100, null=True)),
                ('ct_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('hc_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('hc_code', models.CharField(blank=True, max_length=5, null=True)),
                ('offense_category_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_offense_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsPropDescType',
            fields=[
                ('prop_desc_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('prop_desc_code', models.CharField(blank=True, max_length=2, null=True)),
                ('prop_desc_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_prop_desc_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsProperty',
            fields=[
                ('property_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stolen_count', models.SmallIntegerField(blank=True, null=True)),
                ('recovered_count', models.SmallIntegerField(blank=True, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsIncident')),
            ],
            options={
                'db_table': 'nibrs_property',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsPropertyDesc',
            fields=[
                ('property_value', models.BigIntegerField(blank=True, null=True)),
                ('date_recovered', models.DateTimeField(blank=True, null=True)),
                ('nibrs_prop_desc_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('prop_desc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsPropDescType')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsProperty')),
            ],
            options={
                'db_table': 'nibrs_property_desc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsPropLossType',
            fields=[
                ('prop_loss_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('prop_loss_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_prop_loss_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsRelationship',
            fields=[
                ('relationship_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('relationship_code', models.CharField(blank=True, max_length=2, null=True)),
                ('relationship_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_relationship',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsSumMonthTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nibrs_month_id', models.BigIntegerField(blank=True, null=True)),
                ('agency_id', models.BigIntegerField(blank=True, null=True)),
                ('month_num', models.SmallIntegerField(blank=True, null=True)),
                ('data_year', models.SmallIntegerField(blank=True, null=True)),
                ('reported_status', models.CharField(blank=True, max_length=1, null=True)),
                ('report_date', models.DateTimeField(blank=True, null=True)),
                ('prepared_date', models.DateTimeField(blank=True, null=True)),
                ('orig_format', models.CharField(blank=True, max_length=1, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('data_home', models.CharField(blank=True, max_length=1, null=True)),
                ('ddocname', models.CharField(blank=True, max_length=50, null=True)),
                ('did', models.BigIntegerField(blank=True, null=True)),
                ('nibrs_ct_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('nibrs_hc_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('nibrs_leoka_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('nibrs_arson_flag', models.CharField(blank=True, max_length=1, null=True)),
                ('nibrs_ht_flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'nibrs_sum_month_temp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsSuspectedDrug',
            fields=[
                ('est_drug_qty', models.FloatField(blank=True, null=True)),
                ('nibrs_suspected_drug_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('drug_measure_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsDrugMeasureType')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsProperty')),
            ],
            options={
                'db_table': 'nibrs_suspected_drug',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsSuspectedDrugType',
            fields=[
                ('suspected_drug_type_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('suspected_drug_code', models.CharField(blank=True, max_length=1, null=True)),
                ('suspected_drug_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_suspected_drug_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsSuspectUsing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offense', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffense')),
            ],
            options={
                'db_table': 'nibrs_suspect_using',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsUsingList',
            fields=[
                ('suspect_using_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('suspect_using_code', models.CharField(blank=True, max_length=1, null=True)),
                ('suspect_using_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_using_list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsVictim',
            fields=[
                ('victim_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('victim_seq_num', models.SmallIntegerField(blank=True, null=True)),
                ('outside_agency_id', models.BigIntegerField(blank=True, null=True)),
                ('age_num', models.SmallIntegerField(blank=True, null=True)),
                ('sex_code', models.CharField(blank=True, max_length=1, null=True)),
                ('resident_status_code', models.CharField(blank=True, max_length=1, null=True)),
                ('agency_data_year', models.SmallIntegerField(blank=True, null=True)),
                ('ff_line_number', models.BigIntegerField(blank=True, null=True)),
                ('age_range_low_num', models.SmallIntegerField(blank=True, null=True)),
                ('age_range_high_num', models.SmallIntegerField(blank=True, null=True)),
                ('activity_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsActivityType')),
                ('age', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsAge')),
                ('assignment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsAssignmentType')),
                ('ethnicity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsEthnicity')),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsIncident')),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ref.RefRace')),
            ],
            options={
                'db_table': 'nibrs_victim',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsVictimCircumstances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circumstances', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsCircumstances')),
                ('justifiable_force', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsJustifiableForce')),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsVictim')),
            ],
            options={
                'db_table': 'nibrs_victim_circumstances',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsVictimInjury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injury', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsInjury')),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsVictim')),
            ],
            options={
                'db_table': 'nibrs_victim_injury',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsVictimOffenderRel',
            fields=[
                ('nibrs_victim_offender_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('offender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffender')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsRelationship')),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsVictim')),
            ],
            options={
                'db_table': 'nibrs_victim_offender_rel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsVictimOffense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offense', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffense')),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsVictim')),
            ],
            options={
                'db_table': 'nibrs_victim_offense',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsVictimType',
            fields=[
                ('victim_type_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('victim_type_code', models.CharField(blank=True, max_length=1, null=True)),
                ('victim_type_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nibrs_victim_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsWeapon',
            fields=[
                ('nibrs_weapon_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('offense', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffense')),
            ],
            options={
                'db_table': 'nibrs_weapon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NibrsWeaponType',
            fields=[
                ('weapon_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('weapon_code', models.CharField(blank=True, max_length=3, null=True)),
                ('weapon_name', models.CharField(blank=True, max_length=100, null=True)),
                ('shr_flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'nibrs_weapon_type',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='nibrsweapon',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsWeaponType'),
        ),
        migrations.AddField(
            model_name='nibrsvictim',
            name='victim_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsVictimType'),
        ),
        migrations.AddField(
            model_name='nibrssuspectusing',
            name='suspect_using',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsUsingList'),
        ),
        migrations.AddField(
            model_name='nibrssuspecteddrug',
            name='suspected_drug_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsSuspectedDrugType'),
        ),
        migrations.AddField(
            model_name='nibrsproperty',
            name='prop_loss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsPropLossType'),
        ),
        migrations.AddField(
            model_name='nibrsoffense',
            name='offense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffenseType'),
        ),
        migrations.AddField(
            model_name='nibrsincident',
            name='nibrs_month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsMonth'),
        ),
        migrations.AddField(
            model_name='nibrsgrpbarrestweapon',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsWeaponType'),
        ),
        migrations.AddField(
            model_name='nibrsgrpbarrest',
            name='nibrs_month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsMonth'),
        ),
        migrations.AddField(
            model_name='nibrsgrpbarrest',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ref.RefRace'),
        ),
        migrations.AddField(
            model_name='nibrscriminalact',
            name='criminal_act',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsCriminalActType'),
        ),
        migrations.AddField(
            model_name='nibrscriminalact',
            name='offense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffense'),
        ),
        migrations.AddField(
            model_name='nibrsbiasmotivation',
            name='offense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffense'),
        ),
        migrations.AddField(
            model_name='nibrsarresteeweapon',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsWeaponType'),
        ),
        migrations.AddField(
            model_name='nibrsarrestee',
            name='arrest_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsArrestType'),
        ),
        migrations.AddField(
            model_name='nibrsarrestee',
            name='ethnicity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsEthnicity'),
        ),
        migrations.AddField(
            model_name='nibrsarrestee',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsIncident'),
        ),
        migrations.AddField(
            model_name='nibrsarrestee',
            name='offense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nibrs.NibrsOffenseType'),
        ),
        migrations.AddField(
            model_name='nibrsarrestee',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ref.RefRace'),
        ),
        migrations.AlterUniqueTogether(
            name='nibrsvictimoffense',
            unique_together=set([('victim', 'offense')]),
        ),
        migrations.AlterUniqueTogether(
            name='nibrsvictiminjury',
            unique_together=set([('victim', 'injury')]),
        ),
        migrations.AlterUniqueTogether(
            name='nibrsvictimcircumstances',
            unique_together=set([('victim', 'circumstances')]),
        ),
        migrations.AlterUniqueTogether(
            name='nibrssuspectusing',
            unique_together=set([('suspect_using', 'offense')]),
        ),
        migrations.AlterUniqueTogether(
            name='nibrsmonth',
            unique_together=set([('agency', 'month_num', 'data_year', 'data_home')]),
        ),
        migrations.AlterUniqueTogether(
            name='nibrscriminalact',
            unique_together=set([('criminal_act', 'offense')]),
        ),
        migrations.AlterUniqueTogether(
            name='nibrsbiasmotivation',
            unique_together=set([('bias', 'offense')]),
        ),
    ]
