from jinja2 import Environment, FileSystemLoader
import yaml
env = Environment(loader=FileSystemLoader('.'))
def get_interface_speed(interface_name):
    """Return Mbps speed based on interface name keywords"""
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100
    return 'Unknown'
env.filters['get_interface_speed'] = get_interface_speed
template = env.get_template("template-task8.j2")
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)
output = template.render(interface_list=interfaces)
print(output)

