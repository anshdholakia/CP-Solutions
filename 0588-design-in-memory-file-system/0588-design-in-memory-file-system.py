class Directory:
    def __init__(self, name):
        self.name = name
        self.children={} # key is going to be the name: value is the object
    
class File:
    def __init__(self, name, content=""):
        self.name=name
        self.content=content

class FileSystem:

    def __init__(self):
        self.root=Directory('/')

    def ls(self, path: str, cur_dir=None) -> List[str]:
        # use dfs to go to the path and get the children
        cur_dir=self.root if cur_dir==None else cur_dir
        if not cur_dir:
            return []
        splitted_path=path.split('/')
        if splitted_path and splitted_path[0]=='':
            splitted_path=splitted_path[1:]
        if splitted_path:
            return self.ls("/".join(splitted_path[1:]), cur_dir.children.get(splitted_path[0], None))
        if isinstance(cur_dir, File):
            return [cur_dir.name]
        return sorted([x for x in cur_dir.children])

    def mkdir(self, path: str, cur_dir=None) -> None:
        cur_dir=self.root if cur_dir==None else cur_dir
        if not path:
            return
        splitted_path=path.split('/')
        if splitted_path and splitted_path[0]=='':
            splitted_path=splitted_path[1:]
        cur_dir.children[splitted_path[0]] = cur_dir.children.get(splitted_path[0], Directory(splitted_path[0]))
        self.mkdir("/".join(splitted_path[1:]), cur_dir.children[splitted_path[0]])

    def addContentToFile(self, filePath: str, content: str, cur_dir=None) -> None:
        cur_dir=self.root if cur_dir==None else cur_dir
        splitted_path=filePath.split('/')
        if splitted_path and splitted_path[0]=='':
            splitted_path=splitted_path[1:]
        if len(splitted_path)==1:
            cur_dir.children[splitted_path[0]]=cur_dir.children.get(splitted_path[0], File(splitted_path[0]))
            cur_dir.children[splitted_path[0]].content+=content
            return
        self.addContentToFile("/".join(splitted_path[1:]), content, cur_dir.children[splitted_path[0]])

    def readContentFromFile(self, filePath: str, cur_dir=None) -> str:
        cur_dir=self.root if cur_dir==None else cur_dir
        splitted_path=filePath.split('/')
        if splitted_path and splitted_path[0]=='':
            splitted_path=splitted_path[1:]
        if len(splitted_path)==1:
            return cur_dir.children[splitted_path[0]].content
        return self.readContentFromFile("/".join(splitted_path[1:]), cur_dir.children[splitted_path[0]])


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)