import socket

server = socket.socket()
server.bind(("localhost", 9999))
server.listen(5)
cliente, datos = server.accept()
mensaje = cliente.recv(1024)
print mensaje

