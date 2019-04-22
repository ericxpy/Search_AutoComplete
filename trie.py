class Node(object):
    def __init__(self):

        self.children={}
        self.complete=False
        self.ID=[]
        self.type=[]
        """
        type:
        "nm":NameMain
        "ng":NameGeneric
        "nb":NamesBrand
        "mc":Mechanisms
        "nc":NamesCode
        """
        

class Trie(object):
    def __init__(self):
        
        
        self.root=Node()
        

    def insert(self, word, ID, type):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node=self.root
        for i in word:
            if i not in node.children:
                node.children[i]=Node()
            node=node.children[i]
        
        node.complete=True
        node.ID.append(ID)
        node.type.append(type)
        

    def find(self, prefix, k):
        """
        Returns top k words starting with the prefix
        :type prefix: str
        :rtype: list of str
        """
        node=self.root
        res=[]
        for i in prefix:
            if i in node.children:
                node=node.children[i]
            else:
                return []
        def dfs(node,curr):
            if node.complete:
                for j,ID in enumerate(node.ID):
                    res.append([curr,ID,node.type[j]])

            for i in node.children:
                dfs(node.children[i],curr+i)



        dfs(node,prefix)

        return res[:k]
