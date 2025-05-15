import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML data
with open("devices.yaml") as f:
    data = yaml.safe_load(f)

# Set up Jinja2 environment to look for templates in the current directory
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("interface_template.j2")

# Loop through each router and generate config
for router in data['routers']:
    config = template.render(router=router)
    filename = f"{router['name']}_config.txt"
    with open(filename, "w") as output_file:
        output_file.write(config)
    print(f"Configuration for {router['name']} written to {filename}")

