import socket
import time

server = socket.socket()

connection = server.connect(("localhost", 9999))
time.sleep(1)
connection.send("Manteca de cacao")
connection.close()
