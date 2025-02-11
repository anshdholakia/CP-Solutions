class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        idx=0
        current_str=""
        path+='/'
        while idx<len(path):
            if path[idx]=='/':
                # TODO
                if current_str=="..":
                    if stack:
                        stack.pop()
                elif current_str and current_str!='.':
                    stack.append(current_str)
                current_str=""
            else:
                current_str+=path[idx]
            idx+=1
        return "/"+"/".join(stack)