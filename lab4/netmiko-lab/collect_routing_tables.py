import yaml
from netmiko import Netmiko

# Export required if using TextFSM
import os
os.environ["NET_TEXTFSM"] = "ntc-templates/ntc_templates/templates"

devices = yaml.safe_load(open("lab_devices.yml"))

for device in devices["devices"]:
    try:
        net_connect = Netmiko(ip=device["ip"],
                              username=device["username"],
                              password=device["password"],
                              port=device["port"],
                              device_type=device["device_type"])

        output = net_connect.send_command("show ip route", use_textfsm=True)
        print(f"\nRouting Table for {device['name']}:\n")
        for route in output:
            print(f"Protocol: {route['protocol']}, Network: {route['network']}, "
                  f"Mask: {route['mask']}, Next Hop: {route.get('nexthop', '-')}, "
                  f"Distance/Metric: {route.get('distance_metric', '-')}")
        net_connect.disconnect()

    except Exception as e:
        print(f"Error collecting routing table from {device['name']}: {str(e)}")


