import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9090

msg = 'Hello World'

# connection to hostname on the port.
s.connect((host, port))
s.send(msg.encode('ascii'))
# Receive no more than 1024 bytes

s.close()


