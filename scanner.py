import socket
import argparse
import sys

#

def validate_port_range_syntax(port_ranges):
    for i in range(0, len(port_ranges)-2):
        if((',' not in port_ranges[i]) and (',' not in port_ranges[i+1]) and (',' not in port_ranges[i+2])):
            print('invalid port range')
            sys.exit()
    for port_range in port_ranges:
        if(port_range[-1] == ',' or port_range[0] == ','):
            print('invalid port range')
            sys.exit()

def validate_port_range_low_to_high(low_port, high_port):
    if(int(low_port) >= int(high_port)):
        print("In a port range (i.e. 5-10) the first port should be strictly lower than the last.")
        print(f"ERROR: {low_port} is greater than or equal to {high_port} in range '{low_port}-{high_port}'")

def get_ports_from_range(low_port, high_port):
    return list(range(int(low_port), int(high_port)))

def parse_ports(ports: str) -> list:
    port_ranges = ports.split('-')
    validate_port_range_syntax(port_ranges)
    final_ports_to_scan = []
    for i in range(0, len(port_ranges)-1):

        port_range_low = port_ranges[i].split(',')
        port_range_high = port_ranges[i+1].split(',')
        
        low_port = port_range_low[-1]
        high_port = port_range_high[0]
        validate_port_range_low_to_high(low_port, high_port)
        ports_from_range = get_ports_from_range(low_port, high_port)
        final_ports_to_scan += port_range_low[0:-1]
        final_ports_to_scan += ports_from_range

    final_ports_to_scan += port_ranges[-1].split(',')[0:]

    return final_ports_to_scan

parser = argparse.ArgumentParser(
    prog="practice-scanner",
    description="Small little scanner I made to practice the socket library we cover in TCMs PNPT",
    epilog="To whomever may read this: You are beautiful and belong here in the world <3"
)

parser.add_argument('host')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-p', '--ports', action='store', help='Arguments can be in the formats:\nstart-end port\nport (single)\nport1,port2,...,portn', required=True)

args = parser.parse_args()
parse_ports(args.ports)
verbose=args.verbose
host=args.host

ports=parse_ports(args.ports)

closed_ports = []
open_ports = []


scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[+] Initiating scan...")
if(verbose):
    print("[+] Ports to scan: {}", ports)
for port in ports:
    connection_info = (host,port)
    try:
        scanner.connect(connection_info)
        open_ports.append(port)
        if(verbose):
            print(f'[+] Verbose scan: Port {port} open')
    except:
        closed_ports.append(port)
        if(verbose):
            print(f'[+] Verbose scan: Port {port} closed')
print("\n")
print(f"[+] {len(open_ports)} open.")
print(f"[+] {len(closed_ports)} closed (not reachable; may be filtered).")

for port in open_ports:
    print(f"Port {port} OPEN")

