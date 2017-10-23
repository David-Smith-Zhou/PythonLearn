# -*- coding: utf-8 -*- f
__author__ = "DavidSmith"
__job__ = "Test"

import socket
import traceback


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except Exception as e:
        traceback.print_exc()
    s.send(bytes("hello socketserver", "utf-8"))
    # s.close()
    print("send end")
    buf = s.recv(4096)
    if not len(buf):
        print(buf)
    s.close()
    print("client over")
