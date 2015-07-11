import os

class bower:
    def __init__(self, site, path=None):
        self.site = site
        self.path = path

    def created(self, port=80):
        print('Create directory:')
        print(self.path + "\n")

        text = """#created by site.py
        <VirtualHost *:%s>
            ServerName %s
            ServerAdmin webmaster@localhost
            DocumentRoot %r
            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>""" % (port, self.site, self.path)

        # conf = open('/etc/apache2/sites-available/%s.conf' % self.site, 'w+')
        conf = open('/tmp/%s.conf' % self.site, 'w+')
        conf.write(text)
        conf.close()

        os.system("sudo mv /tmp/%s.conf /etc/apache2/sites-available/%s.conf" % (self.site,self.site))

        print('Create apache2 config:')
        print(text + '\n')

        os.system("sudo a2ensite %s" % self.site)
        self.save()

    def remove(self):
        print("Removing %s..." % self.site)
        if os.path.exists("/etc/apache2/sites-available/%s.conf" % self.site) is True:
            os.system("sudo a2dissite %s" % self.site)
            os.system("sudo rm /etc/apache2/sites-available/%s.conf" % self.site)
        else:
            print("NO ACTION: Site does not exist")

        print("Site successfully removed, but created directories were kept.")

        self.save()

    def save(self):
        os.system("sudo service apache2 reload")
        os.system("sudo service apache2 restart")
