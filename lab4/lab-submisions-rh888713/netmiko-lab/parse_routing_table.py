from netmiko import Netmiko

# Routers list
routers = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": 22},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": 22}
]

for device in routers:
    print(f"\n[+] Connecting to {device['ip']}")
    net_connect = Netmiko(**device)
    routes = net_connect.send_command("show ip route", use_textfsm=True)
    net_connect.disconnect()

    print(f"Routes from {device['ip']}:")
    for route in routes:
        print(f"Protocol: {route.get('protocol')}, "
              f"Network: {route.get('network')}, "
              f"Distance: {route.get('distance')}, "
              f"Metric: {route.get('metric')}")

