#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.6',
    'username': 'so',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.7',
    'username': 'so',
    'password': 'cisco',
}


all_devices = [iosv_l2_s1, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,10):
       print "Creating VLAN " + str(n)
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output 