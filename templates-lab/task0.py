from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')
interface_data = {
    'name': 'GigabitEthernet0/1',
    'description': 'Server Port',
    'vlan': 10
}

output = template.render(interface=interface_data)
print(output)
with open('interface_config.txt', 'w') as f:
    f.write(output)

