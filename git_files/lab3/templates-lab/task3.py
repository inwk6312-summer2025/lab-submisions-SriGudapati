from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template-task3.j2')
interface_data = {
    'description': 'Server Port',
    'vlan': 10
}
output = template.render(interface=interface_data)
print(output)
with open('interface_config_task3.txt', 'w') as f:
    f.write(output)
