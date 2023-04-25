#!/usr/bin/python3.6

import socket
import sys
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# for simplicity the variable will simulate a public key, but no public/private
# key pairs are actually used in this demo
PUBLIC_KEY = "1234-STK-station"

if len(sys.argv) != 3:
    print("Provide ID of a car and its new mileage!")
    print("./update_mileage.py <car_ID> <new_mileage>")
    sys.exit(1)

car_id = sys.argv[1]
new_mileage = int(sys.argv[2])

block = {
    "timestamp": time.ctime(),
    "car": {
        "id": car_id,
        "mileage": new_mileage
    },
    "id": PUBLIC_KEY
}

# send the block to the network
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # in python3 the string must be encoded
    s.sendall(str(block).encode())
    data = s.recv(1024)

print('The block has been received by the network.', repr(data.decode()))
