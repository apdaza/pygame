import socket

s = socket.socket() 
s.connect(("localhost", 5051))

while True:
      mensaje = raw_input("> ")
      s.send(mensaje)
      if s.recv(1024):
          print "->"
      if mensaje == "quit":
         break

print "adios"

s.close()
