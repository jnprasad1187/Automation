from netmiko import ConnectHandler

R01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.241',
    'username': 'cisco',
    'password': 'cisco',
}

R02= {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.242',
    'username': 'cisco',
    'password': 'cisco',
}

with open('all_core_routers_snmp') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [R01, R02]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
