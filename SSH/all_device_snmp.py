from netmiko import ConnectHandler
ISP01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.251',
    'username': 'cisco',
    'password': 'cisco',
}

ISP02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.252',
    'username': 'cisco',
    'password': 'cisco',
}

R01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.241',
    'username': 'cisco',
    'password': 'cisco',
}

R02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.242',
    'username': 'cisco',
    'password': 'cisco',
}

CORE_SW01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.243',
    'username': 'cisco',
    'password': 'cisco',
}

CORE_SW02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.244',
    'username': 'cisco',
    'password': 'cisco',
}

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

with open('all_device_snmp') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [ISP01, ISP02,R01,R02, CORE_SW01, CORE_SW02, ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

