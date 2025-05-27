import yaml
from netmiko import Netmiko
from jinja2 import Environment, FileSystemLoader
import logging

# Logging setup
logging.basicConfig(filename='lab_deploy.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Load YAML files
devices = yaml.safe_load(open("lab_devices.yml"))
env = Environment(loader=FileSystemLoader("."))

template = env.get_template("lab_config_template.j2")

for device in devices["devices"]:
    try:
        net_connect = Netmiko(ip=device["ip"],
                              username=device["username"],
                              password=device["password"],
                              port=device["port"],
                              device_type=device["device_type"])

        config = template.render(hostname=device["hostname"], loopback_id=device["ip"].split(".")[-1])
        output = net_connect.send_config_set(config.split('\n'))
        print(f"Config pushed to {device['name']}")
        logging.info(f"Config pushed to {device['name']}:\n{output}")
        net_connect.disconnect()

    except Exception as e:
        logging.error(f"Failed on {device['name']} - {str(e)}")

