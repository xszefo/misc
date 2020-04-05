#!/usr/bin/python

from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse
import time
import concurrent.futures


ipki = [
'10.100.2.72',
'10.100.2.73',
'10.100.2.91',
'10.100.2.100',
'10.100.2.101',
'10.100.2.102',
'10.100.2.140',
'10.100.2.141',
'10.100.2.142',
'10.100.2.143',
'10.100.2.144',
'10.100.2.145',
'10.100.2.146',
'10.100.2.147',
'10.100.2.148',
'10.100.2.149',
'10.100.2.150',
'10.100.2.151',
'10.100.2.165',
'10.100.2.166',
'10.100.2.221',
'10.100.2.222',
'10.100.2.229',
'10.100.2.101',
'10.100.2.102',
'10.100.2.220',
'10.100.2.156',
'10.100.2.110',
]
pudla = {
'10.100.2.14': 'SW0324',
'10.100.2.15': 'SW0325',
'10.100.2.72': 'SW0326',
'10.100.2.73': 'SW0327',
'10.100.2.91': 'SW0328',
'10.100.2.100': 'SW0349',
'10.100.2.101': 'SW0333',
'10.100.2.102': 'SW0334',
'10.100.2.140': 'SW0301',
'10.100.2.141': 'SW0302',
'10.100.2.142': 'SW0303',
'10.100.2.143': 'SW0304',
'10.100.2.144': 'SW0305',
'10.100.2.145': 'SW0306',
'10.100.2.146': 'SW0307',
'10.100.2.147': 'SW0308',
'10.100.2.148': 'SW0309',
'10.100.2.149': 'SW0310',
'10.100.2.150': 'SW0311',
'10.100.2.151': 'SW0312',
'10.100.2.165': 'SW0316',
'10.100.2.166': 'SW0317',
'10.100.2.190': 'SW0335',
'10.100.2.191': 'SW0336',
'10.100.2.221': 'SW0318',
'10.100.2.222': 'SW0319',
'10.100.2.226': 'SW0321',
'10.100.2.229': 'SW0345',
'10.100.2.238': 'SW0322',
'10.100.2.239': 'SW0323',
'10.100.2.101': 'SW0333',
'10.100.2.102': 'SW0334',
'10.100.2.220': 'SW0341',
'10.100.2.156': 'SW0344',
#'10.100.2.110': 'SW0330',
'10.100.2.211': 'SW0350',
}

user = 'psroot'
passw = getpass('Password: ')

def get_interfaces(ip):
    wynik = ''
    cisco = {
        'device_type' : 'cisco_ios',
        'ip'       : ip,
        'username' : user,
        'password' : passw,
        'secret'   : 'dupa.9',
        }

#device = ConnectHandler(device_type = platform, ip = host, username=username, password=password)
    print('Connecting to {}: {}'.format(pudla[ip], ip))
    try:
        device = ConnectHandler(**cisco)
        device.enable()

        output = device.send_command_expect('show ntp status')
#output = device.send_command('show interface description | inc king')
        wynik_temp = ''
        for line in output.splitlines():
            if 'Vl' not in line and 'Status' not in line and 'RT020' not in line and 'RT0322' not in line:
                wynik += pudla[ip] + ' ; ' + line + '\n'
                wynik_temp += pudla[ip] + ' ; ' + line + '\n'

        sciezka = 'CONFIGI/{}'.format(pudla[ip])
        with open(sciezka, 'w') as x:
                x.write(wynik_temp)
        return wynik_temp

    except Exception as err:
        print('Blad: {} ****************************'.format(ip))

    return True


def main():
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futs = [ executor.submit(get_interfaces, ip) for ip in ipki]
        #for ip in ipki:
    #    get_interfaces(ip)

    print('Czas wykonania programu: {}'.format(time.time()-start))

if __name__ == '__main__':
    main()

