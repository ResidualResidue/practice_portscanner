import socket

verbose=False

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


