from netmiko import Netmiko

# List of all routers
routers = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": 22},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": 22},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": 22},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": 22}
]

for device in routers:
    print(f"\n[+] Connecting to {device['ip']}")
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show ip interface brief", use_textfsm=True)
    net_connect.disconnect()

    print(f"interfaces on {device['ip']}:")
    for interface in output:
        print(f" - {interface['interface']}")


