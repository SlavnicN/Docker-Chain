import socket

peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peer.bind(('localhost', 5000))

while True:
	peer.listen(5)

	client, address = peer.accept()
	print "{} Connected".format(address)

	response = client.recv(255)
	if response != "":
		print response

print 'Close'
client.close()
peer.close()

