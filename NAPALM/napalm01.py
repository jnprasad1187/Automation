
# (.venv) ┌──(.venv)─(joseph㉿ubuntu-VirtualBox)-[~/Ansible_MasterClass/NAPALM]
# └─$ cat napalm1.py

import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.86.243', 'cisco', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_arp_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_bgp_config()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_bgp_config()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_bgp_neighbors_detail()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_config()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_environment()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_interfaces()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_interfaces_counters()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_interfaces_ip()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_ipv6_neighbors_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_lldp_neighbors()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_lldp_neighbors_detail()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_network_instances()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_ntp_peers()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_ntp_stats()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_optics()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_probes_config()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_snmp_information()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_users()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_vlans()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.is_alive()
print (json.dumps(ios_output, indent=4))


                                                                                                                                                 
#(.venv) ┌──(.venv)─(joseph㉿ubuntu-VirtualBox)-[~/Ansible_MasterClass/NAPALM]
#└─$ 
