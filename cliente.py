import socket
import time

server = socket.socket()

connection = server.connect(("localhost", 9999))
time.sleep(1)
connection.send("Oh si nena")
connection.close()
