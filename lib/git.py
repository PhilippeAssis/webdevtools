import os

class Git:
    def __init__(self, remote, path = ""):
        self.remote = remote
        self.path = path

    def clone(self):
        os.system("git clone %s %s" % (self.remote, self.path))



