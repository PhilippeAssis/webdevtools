import os

from lib.tools import tools

class apache2:
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

        conf = open('/etc/apache2/sites-available/%s.conf' % self.site, 'w+')
        conf.write(text)
        conf.close()

        print('Create apache2 config:')
        print(text + '\n')

        os.system("sudo a2ensite %s" % self.site)
        return;

    def remove(self, path=False):
        print("Removing %s..." % self.site)
        if os.path.exists("/etc/apache2/sites-available/%s.conf" % self.site) is True:
            os.system("sudo a2dissite %s" % self.site)
            os.remove("/etc/apache2/sites-available/%s.conf" % self.site)
        else:
            print("NO ACTION: Site does not exist")

        if path is True and self.path is not None:
            if tools.query("Are you sure you want to remove the directory, it will be deleted altogether?",
                           'no') is True:
                os.system("sudo rm -R %s" % self.path)

        print("Site successfully removed, but created directories were kept. They must be removed manually.")
        return;

    def __iter__(self):
        os.system("sudo service apache2 reload")
        os.system("sudo service apache2 restart")