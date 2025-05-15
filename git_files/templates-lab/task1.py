from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')
class NetworkInterface:
    def __init__(self, name, description, vlan):
        self.name = name
        self.description = description
        self.vlan = vlan
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)
output = template.render(interface=interface_obj)
print(output)
with open('interface_config.txt', 'w') as f:
    f.write(output)
