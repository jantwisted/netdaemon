# -*- coding: utf-8 -*-
import socket
import sys
import json
import datetime
import requests
import threading

"""Main module."""

url = "http://lab.funneaty.com/api/update"
p01_port = 30101
p02_port = 9090


def CreateServerInstance_tcp(port):
    s_descriptor_front = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_front = socket.gethostname()
    port_front = port
    s_descriptor_front.bind((host_front, port_front))
    return s_descriptor_front


def CreateServerInstance_Tcp(port):
    s_descriptor_front = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_front = socket.gethostname()
    port_front = port
    print('starting up on {} port {}'.format(*(host_front, port_front)))
    s_descriptor_front.bind((host_front, port_front))
    return s_descriptor_front

def CreateServerInstance_Udp(port):
    s_descriptor_front = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_front = socket.gethostname()
    port_front = port
    print('starting up on {} port {}'.format(*(host_front, port_front)))
    s_descriptor_front.bind((host_front, port_front))
    return s_descriptor_front


def ReplyStrFrontEndModule(client_connection_dict):
    client_connection_str = json.dumps(client_connection_dict)
    client_connection_json = json.loads(client_connection_str)
    return client_connection_json


def PostResultToAPI(client_json):
    api_request = requests.post(url, data=client_json)
    print(api_request.content)
    print(api_request.status_code, api_request.reason)


def LoadPuzzle():
    p0 = threading.Thread(name='puzzle00', target=Puzzle_01)
    p1 = threading.Thread(name='puzzle01', target=Puzzle_02)
    p0.start()
    p1.start()

def ConstructJSON(received_msg, addr, puzzle_number):
    client_dict = {}
    client_dict['client_addr'] = str(addr[0])
    client_dict['client_token'] = received_msg.decode('ascii')
    client_dict['client_con_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_dict['puzzle_number'] = puzzle_number
    client_json = ReplyStrFrontEndModule(client_dict)
    print(json.dumps(client_json, indent=2, sort_keys=True))
    return client_json


def Puzzle_01(port_number=p02_port):
    puzzle_number = 1
    server_socket = CreateServerInstance_Tcp(port_number)
    server_socket.listen(5)
    while 1:
        clientsocket, addr = server_socket.accept()
        msg = clientsocket.recv(1024)
        client_json = ConstructJSON(msg, addr, puzzle_number)
        PostResultToAPI(client_json)
        clientsocket.close()


def Puzzle_02(port_number=p01_port):
    puzzle_number = 2
    server_socket = CreateServerInstance_Udp(port_number)
    while 1:
        msg, addr = server_socket.recvfrom(1024)
        client_json = ConstructJSON(msg, addr, puzzle_number)
        PostResultToAPI(client_json)


if __name__=='__main__':
   LoadPuzzle()
