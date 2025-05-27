from netmiko import Netmiko

# Define the device information
devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",  # Replace with your actual device IP
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

# Configuration commands to add Loopback interface
loopback_config = [
    "interface Loopback10",
    "description Loopback interface added via Netmiko",
    "ip address 10.10.10.10 255.255.255.255",
    "no shutdown"
]

# Loop over devices and push configuration
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(loopback_config)
    print(output)
    net_connect.disconnect()

