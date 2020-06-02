import xmlrpc.client
import socket
import random
import time

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy: #change localhost into IP server
    x = 0
    y = random.randint(3,7)
    while x < y:
        time.sleep(8)
        a = proxy.avg_temp()
        print ("Temperature average : ",a)
    
