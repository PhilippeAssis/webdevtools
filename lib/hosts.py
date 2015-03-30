class hosts:
    def __init__(self, site, ip='127.0.0.1'):
        self.site = site
        self.ip = ip
        with open('/etc/hosts', 'r') as file:
            self.data = file.readlines()

    def remove(self):
        for i, line in enumerate(self.data):
            if self.site in line:
                self.data[i] = ''
                print("Host %s removed!" % self.site)

    def created(self):
        for i, line in enumerate(self.data):
            if self.site in line:
                self.data[i] = self.ip + ' ' + self.site + '\n'
                print("Host %s modified!" % self.site)
                break

            if line in ['\n', '\r\n']:
                self.data[i] = self.ip + ' ' + self.site + '\n\n'
                print("Host %s added!" % self.site)
                break
            elif line in ['\n', '\r\n']:
                print("NO ACTION: Host does not exist, so it can not be removed.")
                break

    def save(self):
        data = ''.join(self.data)
        conf = open('/etc/hosts','w+')
        conf.write(data)
        conf.close()