from netmiko import ConnectHandler

# List of all routers in the topology
routers = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"}
]

# Loop through all routers and print interface descriptions
for device in routers:
        # Inside the for-loop from the above script
    show_cmds = [
        "show version",
        "show ip interface brief",
        "show ip route",
        "show running-config | section interface Loopback"
    ]

    for cmd in show_cmds:
        print(f"\nCommand: {cmd}")
        result = net_connect.send_command(cmd)
        print(result)
        print("=" * 60)

