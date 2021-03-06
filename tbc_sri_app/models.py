from django.db import models

class lnos_statusPipeLine(models.Model):

    container = models.CharField(max_length = 24, blank=True)
    placeofdelivery = models.CharField(max_length = 64, blank=True) #our final place of delivery
    mbol = models.CharField(max_length = 24, blank=True)
    hbol = models.CharField(max_length = 24, blank=True)
    pol = models.CharField(max_length = 64, blank=True)
    carrier = models.CharField(max_length = 24, blank=True)
    bookingnumber = models.CharField(max_length = 128, blank=True)
    vessel = models.CharField(max_length = 40, blank=True)
    voyage = models.CharField(max_length = 40, blank=True)
    destination = models.CharField(max_length = 40, blank=True) #vessel destination
    out_gate = models.CharField(max_length = 128, blank=True)
    return_container = models.CharField(max_length = 128, blank=True)
    empty_equipment_dispatched = models.CharField(max_length = 128, blank=True)
    in_gate = models.CharField(max_length = 128, blank=True)
    vessel_departure = models.CharField(max_length = 128, blank=True)
    vessel_arrival = models.CharField(max_length = 128, blank=True)
    us_customs_hold_at_pod = models.CharField(max_length = 128, blank=True)
    us_customs_hold = models.CharField(max_length = 128, blank=True)
    us_customs_hold_removed = models.CharField(max_length = 128, blank=True)
    customs_released = models.CharField(max_length = 128, blank=True)
    unloaded_from_vessel = models.CharField(max_length = 128, blank=True)
    delivered_to_connecting_line = models.CharField(max_length = 128, blank=True)
    rail_departure_from_origin = models.CharField(max_length = 128, blank=True)
    rail_arrival_at_destination = models.CharField(max_length = 128, blank=True)
    unloaded_from_a_rail_car = models.CharField(max_length = 128, blank=True)
    eta_inbound_door = models.CharField(max_length = 128, blank=True)
    estimated_delivery = models.CharField(max_length = 128, blank=True)
    delivered = models.CharField(max_length = 128, blank=True)
    etd_pol = models.DateTimeField(null=True, blank=True)
    eta_pod = models.DateTimeField(null=True, blank=True)
    eta_placeofdelivery = models.DateTimeField(null=True, blank=True)
    available_for_delivery = models.CharField(max_length = 128, blank=True)
    cargo_received_at_origin = models.CharField(max_length = 128, blank=True)
    carrier_and_customs_release = models.CharField(max_length = 128, blank=True)
    carrier_release = models.CharField(max_length = 128, blank=True)
    estimated_to_arrive = models.CharField(max_length = 128, blank=True)
    loaded_on_barge = models.CharField(max_length = 128, blank=True)
    loaded_on_feeder_vessel = models.CharField(max_length = 128, blank=True)
    loaded_on_truck = models.CharField(max_length = 128, blank=True)
    loaded_on_vessel = models.CharField(max_length = 128, blank=True)
    vessel_arrived_at_transit_port = models.CharField(max_length = 128, blank=True)
    vessel_departed_from_transit_port = models.CharField(max_length = 128, blank=True)




    list_display = ['mbol', 'hbol', 'container', 'customs_released', 'eta_pod', 'unloaded_from_vessel']
