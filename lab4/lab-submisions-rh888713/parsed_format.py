from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123"}
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show ip interface brief", use_textfsm=True)
    print(f"{device['ip']} Interfaces:")
    for interface in output:
        print(f"  {interface['interface']} - {interface['ipaddr']} - {interface['status']}")
    net_connect.disconnect()
output = net_connect.send_command("show ip route", use_textfsm=True)
for route in output:
    print(f"Protocol: {route['protocol']}, Network: {route['network']}, Distance: {route['distance_metric']}")

