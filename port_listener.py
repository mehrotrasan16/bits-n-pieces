# Source : https://pymotw.com/3/socket/tcp.html#echo-server
#socket_echo_server.py

import socket
import sys
import json
import requests

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', 50055)
print('starting up on {} port {}'.format(*server_address))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        
        all_data = b''
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(20480)
            print('received {!r}'.format(data))
            #print(f'\n\n\n{data[512:]}')
            if data:

                if data == b'\x00\x00\x04\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00': #the transmission is complete                    
                   
                    print(f'\n\n\n\nComplete Message: \n {all_data}')
                    data = all_data[512:]                                            #remove the post header
                    try:
                        data = data.decode('utf-8')                                    
                    except Exception as e:
                        print('Decode error', 'Cannot decode message into utf-8')
                    print(f'\n\n\nRemoved 512 byte header data: \n {data}')
                    
                    try:
                        jsonfile = json.loads(data)
                        print(jsonfile.keys())
                        print(jsonfile['hook'].keys())
                    except Exception as e:
                        print("JSON Loading Error","\n\n",str(e),"\n\n\n")
                    
                    print('END Transmission, clearing buffer')
                    all_data = b''
                    
                else:
                    all_data += data                                                #append chunk of 20480 bytes to earlier chunk, until we recieve the end transmission 
            else:
                print('no data from', client_address)
                break
    finally:
        # Clean up the connection
       print(f"Closing Connection Listener on port {server_address[1]}")
       connection.close()

