import socket
import argparse
import sys

parser = argparse.ArgumentParser(
    prog="practice-scanner",
    description="Small little scanner I made to practice the socket library we cover in TCMs PNPT",
    epilog="To whomever may read this: You are beautiful and belong here in the world <3"
)

parser.add_argument('host')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-p', '--ports', action='store', help='Arguments can be in the formats:\nstart-end port\nport (single)\nport1,port2,...,portn')

args = parser.parse_args()

verbose=args.verbose
host=args.host

if(not host or (host == '')):
    print("Invalid arguments")
    sys.exit()

ports=range(0, 100)



scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in ports:
    connection_info = (host,port)
    try:
        scanner.connect(connection_info)
        print(f'Port {port} open')
    except:
        if(verbose):
            print(f'Port {port} closed')


