from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from .models import lnos_statusPipeLine

class lnos_statusPipeLineResource(resources.ModelResource):
    # Use the ForeignKeyWidget to lookup a related model using “natural keys”, i.e., lookup without using the Primary Key (“id”).
    # https://django-import-export.readthedocs.io/en/latest/api_widgets.html

    class Meta:
        model = lnos_statusPipeLine
        skip_unchanged = True
        import_id_fields = (
            'carrier',
            'vessel',
            'voyage',
            'destination',
            'mbol',
            'hbol',
            'container',
            'out_gate',
            'return_container',
            'empty_equipment_dispatched',
            'in_gate',
            'vessel_departure',
            'vessel_arrival',
            'us_customs_hold_at_pod',
            'us_customs_hold',
            'us_customs_hold_removed',
            'customs_released',
            'unloaded_from_vessel',
            'delivered_to_connecting_line',
            'rail_departure_from_origin',
            'rail_arrival_at_destination',
            'unloaded_from_a_rail_car',
            'eta_inbound_door',
            'estimated_delivery',
            'delivered',
            'pol',
            'placeofdelivery',
            'etd_pol',
            'eta_pod',
            'eta_placeofdelivery',
            'available_for_delivery',
            'cargo_received_at_origin',
            'carrier_and_customs_release',
            'carrier_release',
            'estimated_to_arrive',
            'loaded_on_barge',
            'loaded_on_feeder_vessel',
            'loaded_on_truck',
            'loaded_on_vessel',
            'vessel_arrived_at_transit_port',
            'vessel_departed_from_transit_port',
            'bookingnumber',
            )
