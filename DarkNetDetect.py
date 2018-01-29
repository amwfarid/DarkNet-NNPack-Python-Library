import socket
import sys
import subprocess
import time

class DarkNetDetector:

    server_address = ('127.0.0.1', 22666)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self,cfg,weights):
        self.cfg = cfg
        self.weights = weights

    def start(self):
        p = subprocess.Popen("cd $DARKNETNNPACK && ./darknet detect "+str(self.cfg)+" "+str(self.weights)+" XXXXX",shell=True)
        time.sleep(0.5)
        self.sock.connect(self.server_address)

    def detect(self,imageFile):
        try:
            self.sock.sendall(imageFile)
            data = self.sock.recv(4096)
            print data
        except Exception as e:
            print e

    def close(self):
        try:
            self.sock.sendall("exit")
            self.sock.close()
        except Exception as e:
            print e

if __name__ == '__main__':
    d = DarkNetDetector("cfg/yolo.cfg","yolo.weights")
    d.start()
    d.detect("data/eagle.jpg")
    time.sleep(3)
    d.detect("data/person.jpg")
    d.close()
