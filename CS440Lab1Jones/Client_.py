import sys
import socket

conn = socket.socket()
conn.connect(('localhost', 12628))
cmd = raw_input("Enter a command: ")

while cmd != 'q':
    conn.send(cmd)
    data = conn.recv(1024)
    print(str(data))
    cmd = raw_input("Enter a command: ")

conn.close()
