from netmiko import ConnectHandler

CORE_SW01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.243',
    'username': 'cisco',
    'password': 'cisco',
}

with open('core01_switches_spanning_tree') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW01]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
