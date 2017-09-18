import socket

s = socket.socket() 
s.bind(("localhost", 5051))
s.listen(2)

sc1, addr1 = s.accept()
sc2, addr2 = s.accept()

while True:
      recibido1 = sc1.recv(1024)
      recibido2 = sc2.recv(1024)
      if recibido1 == "quit" and recibido2 == "quit":
         break      
      print "Recibido1:", recibido1
      print "Recibido2:", recibido2
      sc1.send(recibido2)
      sc2.send(recibido1)

print "adios"

sc1.close()
sc1.close()
s.close()
