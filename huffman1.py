import queue
import string
r=20
e=4

class HuffmanNode(object):
    def __init__(self,left=None,right=None,root=None):
        self.left = left
        self.right = right
        self.root = root

    def children(self):
        return (self.left,self.right)
    def preorder(self,path=None):
        if path is None:
            nyt = ""
            path = ""
        if self.left is not None:
            if isinstance(self.left[1], HuffmanNode):
                self.left[1].preorder(path+"0")
            else:
                print(self.left,path+"0")
                c1 = self.left[1]
                c2= (ord(c1)-96)
                print(c2)
        if self.right is not None:
            if isinstance(self.right[1], HuffmanNode):
                self.right[1].preorder(path+"1")
            else:
                print(self.right,path+"1")
                c1 = self.right[1]
                c2 = (ord(c1)-96)
                print(c2)

freq = [
    (8, 'a'), (1, 'b'), (2, 'c'), (4, 'd'),
    (12, 'e') ]

def encode(frequencies):
    p = queue.PriorityQueue()
    for item in frequencies:
        p.put(item)

    #invariant that order is ascending in the priority queue
    #p.size() gives list of elements
    
    while p.qsize() > 1:
        left,right = p.get(),p.get()
        node = HuffmanNode(left,right)
        p.put((left[0]+right[0],node))
    return p.get()

node = encode(freq)
print(node[1].preorder())