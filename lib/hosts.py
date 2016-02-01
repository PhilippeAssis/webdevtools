import os

class Hosts:
    def __init__(self, site, ip='127.0.0.1'):
        self.site = site
        self.ip = ip
        with open('/etc/hosts', 'r') as file:
            self.data = file.readlines()

    def remove(self):
        for i, line in enumerate(self.data):
            if self.site in line:
                self.data[i] = ''
                print("Removing %s in host...!" % self.site)

        self.save()

    def created(self):
        for i, line in enumerate(self.data):
            if self.site in line:
                self.data[i] = self.ip + ' ' + self.site + '\n'
                print("modifying %s in host..." % self.site)
                break

            if line in ['\n', '\r\n']:
                self.data[i] = self.ip + ' ' + self.site + '\n\n'
                print("Adding %s in host..." % self.site)
                break
            elif line in ['\n', '\r\n']:
                print("NO ACTION: Host does not exist, so it can not be removed.")
                break

        self.save()


    def save(self):
        data = ''.join(self.data)
        conf = open('/tmp/hosts','w+')
        conf.write(data)
        conf.close()

        os.system("sudo mv /tmp/hosts /etc/hosts")
