import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

server_address = (host, 30101)
message = b'This is a UDP message'

try:
    sent = sock.sendto(message, server_address)
finally:
    sock.close()
