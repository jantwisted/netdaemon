# -*- coding: utf-8 -*-
import socket
import sys
import json
import datetime

"""Main module."""


def CreateServerInstance(port):
    s_descriptor_front = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_front = socket.gethostname()
    port_front = port
    s_descriptor_front.bind((host_front, port_front))
    return s_descriptor_front

def ReplyToFrontEndModule(client_connection_dict):
    client_connection_str = json.dumps(client_connection_dict)
    client_connection_json = json.loads(client_connection_str)
    return client_connection_json

if __name__=='__main__':
    server_socket = CreateServerInstance(9999)
    server_socket.listen(5)
    while 1:
        clientsocket, addr = server_socket.accept()
        msg = clientsocket.recv(1024)
        client_dict = {}
        client_dict['client_addr'] = str(addr[0])
        client_dict['client_token'] = msg.decode('ascii')
        client_dict['client_con_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_dict['puzzle_number'] = "1"
        client_json = ReplyToFrontEndModule(client_dict)
        print(json.dumps(client_json, indent=2, sort_keys=True))
        clientsocket.close()
