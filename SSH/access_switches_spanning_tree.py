from netmiko import ConnectHandler

ACCESS_SW01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.245',
    'username': 'cisco',
    'password': 'cisco',
}

ACCESS_SW02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.246',
    'username': 'cisco',
    'password': 'cisco',
}

ACCESS_SW03 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.247',
    'username': 'cisco',
    'password': 'cisco',
}

with open('access_switches_spanning_tree') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

