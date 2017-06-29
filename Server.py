import socket
import threading
import time
from collections import namedtuple


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.251', 13668))
s.listen(5)
print('Waiting for connection...')
Client = namedtuple("client", ['temp', 'pres', 'dust', 'gas'])
clients = dict()


def cut_string(input_str, head, tail):
    if isinstance(
        head,
        str) and isinstance(
            tail,
            str) and isinstance(
            input_str,
            str):
        start = input_str.find(head) + len(head)
        end = input_str.find(tail, start)

        rt_str = ""
        for index in range(start, end):
            rt_str += input_str[index]
        return rt_str
    else:
        raise TypeError("Inputs are not string!")


def process_connection(sock, addr):
    # print('Accept new connection from %s:%s...' % addr)
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        if data:
            content = bytes(data).decode("utf-8")
            if "E" in content and "G" in content and "P" in content and "D" in content and "T" in content:
                id = cut_string(content, "C", "D")
                sensor = Client(
                    cut_string(
                        content, "T", "P"), cut_string(
                        content, "P", "E"), cut_string(
                        content, "D", "G"), cut_string(
                        content, "G", "T"))
                clients[id] = sensor
                print("ID:" + id + " Temp:" + cut_string(
                    content, "T", "P") + "C Pres:" + cut_string(
                    content, "P", "E") + "hPa Dust:" + cut_string(
                    content, "D", "G") + "ug/cm3 Gas:" + cut_string(
                    content, "G", "T")+"ppm")

    sock.close()
    # print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=process_connection, args=(sock, addr))
    t.start()
