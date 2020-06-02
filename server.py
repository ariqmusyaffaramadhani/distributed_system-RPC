from xmlrpc.server import SimpleXMLRPCServer
import time
import threading

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True) #change the localhost into an IP address
print('connecting to port 8000...')

temps = []

def save_temperature(x,ip):
    temps.append(x)
    print("---------------------------------------")
    print("temprature",x,"º sensed")
server.register_function(save_temperature, "save_temperature")


def show_arr():
    print(temps)
server.register_function(show_arr, "show_arr")


def avg_temp():
    a = 0
    for x in temps:
        a = a + x
    return a/len(temps)
server.register_function(avg_temp, "avg_temp")


class avg_thread(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """
    def __init__(self, interval=8):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            a = 0
            for x in temps:
                a = a + x
            print("_______________________________________")
            print()
            if len(temps) != 0:    
                print("TEMPERATURE AVERAGE : ",a/len(temps))
                print("_______________________________________")
            else:
                print("EMPTY, NO DATA")
                print("_______________________________________")
            time.sleep(self.interval)

ex = avg_thread()

server.serve_forever()