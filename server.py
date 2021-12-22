import socket
import threading

import cv2
import numpy as np

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12395
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(4)


def connection_requests():
    global count
    while True:
        try:
            client_socket, address = server_socket.accept()

            print(f"Connection from {address} has been established")

            t = threading.Thread(target=receive_data, args=(client_socket, ))
            t.start()
        except:
            print(f"{address} disconnected")
            client_socket.close()
            continue


def receive_data(client_socket: socket.socket):
    while True:
        img = client_socket.recv(10064)
        nparr = np.fromstring(img, np.uint8)
        jpeg = cv2.imdecode(nparr, flags=1)
        cv2.imshow("f",jpeg)
        cv2.waitKey(0)


if __name__ == '__main__':
    print(HOST+":"+str(PORT))
    connection_requests()
