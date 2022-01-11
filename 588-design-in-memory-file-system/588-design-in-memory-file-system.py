Trie = lambda: collections.defaultdict(Trie)

class FileSystem(object):
    def __init__(self):
        self.fs = Trie()
        self.fileinfo = collections.defaultdict(str)
        
    def ls(self, path):
        if path in self.fileinfo:
            return path.split('/')[-1:]

        cur = self.fs
        for token in path.split('/'):
            if token in cur:
                cur = cur[token]
            elif token:
                return []

        return sorted(cur.keys())

    def mkdir(self, path):
        cur = self.fs
        for token in path.split('/'):
            if token: cur = cur[token]

    def addContentToFile(self, filePath, content):
        self.mkdir(filePath)
        self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath):
        return self.fileinfo[filePath]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)