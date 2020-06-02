import xmlrpc.client
import socket
import random
import time

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    x = 0
    y = 4
    while x < y:
        print ("")
        print ("Sensing.. ")
        time.sleep(random.randint(1,3))
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name)
        tmp = random.randint(20,40)
        proxy.save_temperature(tmp,host_ip)
        print ("Temperature sensed, sending to server.. ")
        time.sleep(random.randint(1,3))

    
