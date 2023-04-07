import device
from device import Device
from wire import Wire
import wire
import generate_json as genjson

def update_outward_wires_for_devices(devices : dict, wires : dict):
    for wire in wires.values():
        print(wire)
        devices.get(wire.get_send_device_id()).add_outgoing_wire(wire)

def print_all_devices_with_wires(devices : dict):
    for device in devices:
        print(f"{device.get_name()} : ")
        for wire in device.get_all_outgoing_wire():
            print(f"w-{wire.get_id()} ")
        print("\n")