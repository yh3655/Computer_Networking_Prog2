import socket
from socket import *
import time
import sys


def ping(host, port):
    UDPClientSocket = socket(family=AF_INET, type=SOCK_DGRAM)
    UDPClientSocket.settimeout(1)
    server_addr = (host, port)
    resps = []
    for seq in range(1, 11):
        # Send ping message to server and wait for response back
        # On timeouts, you can use the following to add to resps
        # resps.append((seq, ‘Request timed out’, 0))
        # On successful responses, you should instead record the server response and the RTT (must compute server_reply and rtt properly)
        # resps.append((seq, server_reply, rtt))
        # Fill in start
        try:
         start_time = time.time()
         message = "Ping " + str(seq) + " " + str(start_time)
         UDPClientSocket.sendto(message.encode(), server_addr)
         data, server = UDPClientSocket.recvfrom(4096)
         resps.append(data.decode())
         # Fill in end
         print(resps)
        except timeout:
         print("Ping " + str(seq) + " request timed out")

    return resps


if __name__ == '__main__':
    resps = ping('127.0.0.1', 12000)
    print(resps)