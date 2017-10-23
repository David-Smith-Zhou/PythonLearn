# -*- coding: utf-8 -*- f
__author__ = "DavidSmith"
__job__ = "Test"

import random
import socket
import traceback
from time import time, sleep
import _thread


def create_server_socket():
    print("creating socket")
    create_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 8080
    create_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    create_socket.bind((host, port))
    return create_socket


def listen_from_client(socket_name: socket):
    print(socket_name)
    try:
        (client_socket, client_address) = socket_name.accept()
        print("get connect: " + str(client_socket.getpeername()))
        print("socketserver timeout: " + str(client_socket.gettimeout()))
        client_socket.settimeout(10)
        try:

            data = client_socket.recv(4096)
            if len(data) is not 0:
                print("get data from[" + str(client_socket.getpeername) + "]: " + str(data))
        except TimeoutError as te:
            print(te)
            client_socket.close()
        # data = "4D504F53010101007B22737461747573223A223030222C226D7367223A226C6F67696E2073756363657373222C" \
        #        "2264617461223A5B7B22736E223A223030323130313031303031313030303030303037227D2C7B22736E223A22" \
        #        "3030323130313031303031313030303030303038227D2C7B22736E223A22303032313031303130303131303030" \
        #        "3030303133227D2C7B22736E223A223030323130313031303031313030303030303233227D2C7B22736E223A22" \
        #        "3030323130313031303031313030303030303239227D2C7B22736E223A22303032313031303130303131303030" \
        #        "3030303837227D2C7B22736E223A223030323130313031303430313030303030323030227D5D7D4A00"
        # client_socket.send(bytes.fromhex(data))

        # client_socket.send(bytes("\nI get it!", "utf-8"))
        # sleep(5)
        send_by_random(client_socket)
        # no_response()
        try:
            client_socket.close()
        except Exception as e:
            traceback.print_exc()
            print(e)

    except InterruptedError as ie:
        traceback.print_exc()
        print(ie)
    # _thread.exit_thread()


def send_by_random(client_socket: socket):
    rd = random.randint(0, 2)
    if rd is 0:
        print("send source data")
        send_source_data(client_socket)
    elif rd is 1:
        print("send lost data")
        send_lost_data(client_socket)
    else:
        print("no response")
        no_response()


def send_source_data(client_socket: socket):
    data = [
        "12344D",
        "4D504F53010101007B22737461747573223A223030222C226D7367223A226C6F67696E2073756363657373222C",
        "2264617461223A5B7B22736E223A223030323130313031303031313030303030303037227D2C7B22736E223A22",
        "3030323130313031303031313030303030303038227D2C7B22736E223A22303032313031303130303131303030",
        "3030303133227D2C7B22736E223A223030323130313031303031313030303030303233227D2C7B22736E223A22",
        "3030323130313031303031313030303030303239227D2C7B22736E223A22303032313031303130303131303030",
        "3030303837227D2C7B22736E223A223030323130313031303430313030303030323030227D5D7D4A00",
        "1234"
    ]
    for index in range(len(data)):
        send_to_client(client_socket, data[index])


def no_response():
    sleep(11)


def send_lost_data(client_socket: socket):
    data = [
        "12344D",
        "4D504F53010101007B22737461747573223A223030222C226D7367223A226C6F67696E2073756363657373222C",
        "2264617461223A5B7B22736E223A223030323130313031303031313030303030303037227D2C7B22736E223A22",
        "3030323130313031303031313030303030303038227D2C7B22736E223A22303032313031303130303131303030",
        "3030303133227D2C7B22736E223A223030323130313031303031313030303030303233227D2C7B22736E223A22",
        # "3030323130313031303031313030303030303239227D2C7B22736E223A22303032313031303130303131303030",
        "3030303837227D2C7B22736E223A223030323130313031303430313030303030323030227D5D7D4A00",
        "1234"
    ]
    for index in range(len(data)):
        send_to_client(client_socket, data[index])


def run_in_new_thread(socket_name: socket):
    print(socket_name)
    _thread.start_new_thread(listen_from_client, (socket_name, ))


def send_to_client(client_socket: socket, data =  str):
    try:
        client_socket.send(bytes.fromhex(data))
        sleep(0.5)
    except ConnectionAbortedError as ce:
        traceback.print_exc()
        print(ce)
    except ConnectionResetError as cr:
        traceback.print_exc()
        print(cr)


def main():
    s = create_server_socket()
    print(time())
    print("listen....")
    s.listen(1)
    # listen_from_client(s)
    while 1:
        # run_in_new_thread(s)
        listen_from_client(s)

if __name__ == "__main__":
    main()
