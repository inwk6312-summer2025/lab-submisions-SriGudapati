from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"}
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()
    uptime_index = output.find("uptime is")
    print(device["ip"] + " => " + output[uptime_index:uptime_index + 50])
    config_reg_index = output.find("Configuration register is")
    print(device["ip"] + " => " + output[config_reg_index:config_reg_index + 40])
