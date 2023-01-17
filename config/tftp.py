from threading import Thread

import tftpy


class TftpServer:
    def __init__(self, directory, port):
        self.directory = directory
        self.port = port
        self.server = None
        self.thread = None

    def __enter__(self):
        self.server = tftpy.TftpServer(self.directory)

        def start(s):
            s.server.listen("0.0.0.0", s.port, timeout=1)

        self.thread = Thread(target=start, args=(self,))
        self.thread.start()
        return self

    def __exit__(self, type_, value, traceback):
        self.server.stop(now=True)
        self.thread.join()
