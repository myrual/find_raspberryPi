import socket

MCAST_GRP = '255.255.255.255'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))

while True:
	aa, addr = sock.recvfrom(10240)
	print addr
	sock.sendto("pi is here", addr)
