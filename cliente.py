import socket
import time

server = socket.socket()

connection = server.connect(("localhost", 9999))
time.sleep(1)
connection.send("Manteca de cacao")
time.sleep(1)                                                         │
connection.send("Uingardum lebiosa")
time.sleep(1)                                                         │
connection.send("Lumus")
connection.close()

try:
	cliente2 = server.connect(("localhost", 9998))
	cliente2.send("Me quiero volver chango")
except:
	print "Hubo un problema con el segundo cliente"
