# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lnos_statusPipeLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('carrier', models.CharField(max_length=24, blank=True)),
                ('vessel', models.CharField(max_length=40, blank=True)),
                ('voyage', models.CharField(max_length=40, blank=True)),
                ('destination', models.CharField(max_length=40, blank=True)),
                ('mbol', models.CharField(max_length=24, blank=True)),
                ('hbol', models.CharField(max_length=24, blank=True)),
                ('container', models.CharField(max_length=24, blank=True)),
                ('out_gate', models.CharField(max_length=128, blank=True)),
                ('return_container', models.CharField(max_length=128, blank=True)),
                ('empty_equipment_dispatched', models.CharField(max_length=128, blank=True)),
                ('in_gate', models.CharField(max_length=128, blank=True)),
                ('vessel_departure', models.CharField(max_length=128, blank=True)),
                ('vessel_arrival', models.CharField(max_length=128, blank=True)),
                ('us_customs_hold_at_pod', models.CharField(max_length=128, blank=True)),
                ('us_customs_hold', models.CharField(max_length=128, blank=True)),
                ('us_customs_hold_removed', models.CharField(max_length=128, blank=True)),
                ('customs_released', models.CharField(max_length=128, blank=True)),
                ('unloaded_from_vessel', models.CharField(max_length=128, blank=True)),
                ('delivered_to_connecting_line', models.CharField(max_length=128, blank=True)),
                ('rail_departure_from_origin', models.CharField(max_length=128, blank=True)),
                ('rail_arrival_at_destination', models.CharField(max_length=128, blank=True)),
                ('unloaded_from_a_rail_car', models.CharField(max_length=128, blank=True)),
                ('eta_inbound_door', models.CharField(max_length=128, blank=True)),
                ('estimated_delivery', models.CharField(max_length=128, blank=True)),
                ('delivered', models.CharField(max_length=128, blank=True)),
                ('pol', models.CharField(max_length=64, blank=True)),
                ('placeofdelivery', models.CharField(max_length=64, blank=True)),
                ('etd_pol', models.DateTimeField(blank=True, null=True)),
                ('eta_pod', models.DateTimeField(blank=True, null=True)),
                ('eta_placeofdelivery', models.DateTimeField(blank=True, null=True)),
                ('available_for_delivery', models.CharField(max_length=128, blank=True)),
                ('cargo_received_at_origin', models.CharField(max_length=128, blank=True)),
                ('carrier_and_customs_release', models.CharField(max_length=128, blank=True)),
                ('carrier_release', models.CharField(max_length=128, blank=True)),
                ('estimated_to_arrive', models.CharField(max_length=128, blank=True)),
                ('loaded_on_barge', models.CharField(max_length=128, blank=True)),
                ('loaded_on_feeder_vessel', models.CharField(max_length=128, blank=True)),
                ('loaded_on_truck', models.CharField(max_length=128, blank=True)),
                ('loaded_on_vessel', models.CharField(max_length=128, blank=True)),
                ('vessel_arrived_at_transit_port', models.CharField(max_length=128, blank=True)),
                ('vessel_departed_from_transit_port', models.CharField(max_length=128, blank=True)),
                ('bookingnumber', models.CharField(max_length=128, blank=True)),
            ],
        ),
    ]
