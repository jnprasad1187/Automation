from netmiko import ConnectHandler

CORE_SW02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.244',
    'username': 'cisco',
    'password': 'cisco',
}
with open('core02_switches_spanning_tree') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW02]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
