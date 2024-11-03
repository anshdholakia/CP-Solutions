"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res="["
        # the format is going to be par[child(command-sep)]
        if root:
            res+=str(root.val)
            res+=",".join([self.serialize(child) for child in root.children])
        res+=']'
        return res
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        data=data[1:-1]
        if not data:
            return None
        digit=0
        i=0
        for i, c in enumerate(data):
            if not c.isdigit():
                break
            digit=digit*10+int(c)
        node=Node(digit)
        children=[]
        # the way to split woudl be to keep a count of open and close
        b=0
        cur_c=""
        for i, c in enumerate(data[i:]):
            if c=='[':
                b+=1
            elif c==']':
                b-=1
            elif c==',' and b==0:
                children.append(cur_c)
                cur_c=""
                continue
            cur_c+=c
        children.append(cur_c)
        node.children=[self.deserialize(c) for c in children if len(c)>2]
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))