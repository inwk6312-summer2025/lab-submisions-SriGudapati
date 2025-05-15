from jinja2 import Environment, FileSystemLoader
import yaml
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template-task6.j2")
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)
output = template.render(interface_list=interfaces)
print(output)
