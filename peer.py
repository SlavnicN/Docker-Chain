import socket
import threading

class ClientThread(threading.Thread):
	def __init__(self, ip, port, clientsocket):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.clientsocket = clientsocket
		print("[+] New thread  %s %s" %(self.ip, self.port, ))

	def run(self):
		print("conection %s %s" % (self.ip,self.port, ))

		r = self.clientsocket.recv(2048)
		print("reading ",r , "...")
		
		self.clientsocket.send("ok")
		print("Client disconnect")

peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
peer.bind(('localhost', 5000))

while True:
	peer.listen(5)
	print("Listening...")
	(clientsocket, (ip,port)) = peer.accept()
	newthread = ClientThread(ip, port, clientsocket)
	newthread.start()


