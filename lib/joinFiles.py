import os
import fnmatch
import ntpath

class joinFiles:
    comments = {
        'css': '/*\n %s\n*/',
        'html': '<!--\n %s\n-->',
        'py': '"""\n %s\n"""',
        'php': '/*\n t%s\n*/',
        'js': '/*\n %s\n*/'
    }

    type = 'js'

    def find(self, pattern, path, recursive=False):
        result = []
        for root, dirs, files in os.walk(path):
            if recursive is False and root is not path:
                continue

            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))

        return result

    def listFiles(self, files, recursive=False):
        itens = []
        for file in files:
            if os.path.isfile(file) is False:
                if os.sep in file:
                    path = file.split(os.sep)
                    file = path[-1]
                    del path[-1]
                    path = os.sep.join(path)

                if file[0] is '.':
                    find = self.find("*" + file, path, recursive)
                    for item in find:
                        itens.append(item)
            else:
                itens.append(file)

        return itens;

    def comment(self, text):
        try:
            self.comments[self.type]
        except NameError:
            self.type = 'js'

        comment = self.comments[self.type]
        return comment % text

    def merge(self, files, recursive=False):
        files = self.listFiles(files, recursive)

        print('Joining files...')

        self.join = '';
        for file in files:
            print(file + '...')
            with open(file, 'r') as item:
                filedata = ntpath.basename(file) + ' - united with WebDevTools'
                title = self.comment(filedata) + '\n'
                self.join += title + item.read() + '\n'
            print('joined files!')

    def save(self, path):
        conf = open(path, 'w+')
        conf.write(self.join)
        conf.close()
        print('\'%s\' created and saved successfully!' % path)




