from duckdb.duckdb import values


class root:
    def __init__(self,val,left,right):
        self.value = val
        self.right = right
        self.left = left
    def inorder(self):
        res = []
        if self.left:
            res+=self.left.inorder()
        res.append(self.val)
        if self.right:
            res+=self.right.inorder()
        return res
    def preorder(self):
        res=[]
        res.append(self.val)
        if self.left:
            res+self.left.preorder()
        if self.right:
            res+self.right.preorder()
        return res
    def postorder(self):
        res=[]
        if self.left:
            res+self.left.postorder()
        if self.right:
            res+self.right.postorder()
        res.append(self.val)
        return res




