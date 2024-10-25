class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        if '/' in folder_set:
            folder_set.remove('/')
        if '' in folder_set:
            folder_set.remove('')
        for f in folder:
            for i in range(len(f)-1):
                if f[i]=='/' and f[:i] in folder_set:
                    folder_set.remove(f)
                    break
        return list(folder_set)