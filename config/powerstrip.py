import time
from pyegctl.device import EGV21


class PowerStrip:
    def __init__(self, ip, port, password, socket_no):
        self._ps = EGV21(ip, port, password)
        self._socket_no = socket_no
        self._sockets = ["left", "left", "left", "left"]

    def on(self):
        self._sockets[self._socket_no] = "on"
        self._ps.set(self._sockets)

    def off(self):
        self._sockets[self._socket_no] = "off"
        self._ps.set(self._sockets)

    def cycle(self, delay):
        self.off()
        time.sleep(delay)
        self.on()
