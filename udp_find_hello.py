import socket
import time

MCAST_GRP = '<broadcast>'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.settimeout(2)
for i in range(5):
    sock.sendto("robot", (MCAST_GRP, MCAST_PORT))
    try:
        content , addr = sock.recvfrom(1024)
    except :
        continue
    if content == "pi is here":
        print("Found one Pi from " + str(addr))
    time.sleep(1)
