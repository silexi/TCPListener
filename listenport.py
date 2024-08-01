# Author: Bartu KILIÇ
# Contact: kilicbartu@gmail.com
# GitHub: https://github.com/silexi
# Website: https://bartukilic.com

import sys
import socket
import select

def start(IP="127.0.0.1", PORT=443):
    TCP_IP = IP
    TCP_PORT = PORT
    BUFFER_SIZE = 1024
    param = []

    print('Listening for client...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TCP_IP, TCP_PORT))
    server.listen(1)
    rxset = [server]
    txset = []

    while True:
        try:
            rxfds, txfds, exfds = select.select(rxset, txset, rxset)
            for sock in rxfds:
                if sock is server:
                    conn, addr = server.accept()
                    conn.setblocking(0)
                    rxset.append(conn)
                    print('Connection from address:', addr)
                else:
                    try:
                        data = sock.recv(BUFFER_SIZE)
                        if not data or data.decode('utf-8') == ";":
                            print("Received all the data")
                            for x in param:
                                print(x.decode('utf-8'))
                            param = []
                            rxset.remove(sock)
                            sock.close()
                        else:
                            print("Received data: ", data.decode('utf-8'))
                            param.append(data)
                    except:
                        print("Connection closed by remote end")
                        param = []
                        rxset.remove(sock)
                        sock.close()
        except KeyboardInterrupt:
            print("Server is shutting down...")
            server.close()
            break
