import socket

peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
peer.connect(('localhost',5000))
print "Connected to {}".format(5000)

peer.send("I'm connected to you")

print 'Close'
peer.close()