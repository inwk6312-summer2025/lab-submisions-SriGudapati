from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template-task2.j2')
class NetworkInterface:
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10, uplink=True)
output = template.render(interface=interface_obj)
print(output)
with open('interface_config_task2.txt', 'w') as f:
    f.write(output)

