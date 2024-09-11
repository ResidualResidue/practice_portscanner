import socket
import argparse
import sys

parser = argparse.ArgumentParser(
    prog="practice-scanner",
    description="Small little scanner I made to practice the socket library we cover in TCMs PNPT",
    epilog="To whomever may read this: You are beautiful and belong here in the world <3"
)

parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()

verbose=args.verbose

host='192.168.57.1'
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


