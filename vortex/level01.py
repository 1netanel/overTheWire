import socket
import ctypes
HOST = "vortex.labs.overthewire.org"
PORT = 5842
TYPE = "little"

addr = (HOST, PORT)
s = socket.create_connection(addr)

sum = 0

for _ in range(4):
    data = s.recv(4)
    num = int.from_bytes(data, TYPE, signed=False)
    sum += num

msg = sum.to_bytes(32, TYPE, signed=False)

s.send(msg)
data = s.recv(1024)
s.close()
print(repr(data))
