class Tree_Node:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.endhere = False
class Trie:
    def __init__(self,root):
        # "initializing our data structure"
        self.root = Tree_Node(None)
    def insert(self,word):
        main = self.root
        for i,char in enumerate(word):
            # enumerate with 0,a and 1,b for word abc
            if char not  in main.children:
                # cheching for bcd in abc if not then create b node and so on
                main.children[char]=Tree_Node(char)
            # if character present in the children then check for the next character in children
            main = main.children[char]
            if i == len(word)-1:
                main.endhere = True
                
    def search(self,word):
        # it is used for searching the whole word in the trie like abc in abc 
        # and if we are searching abc in abcd then it will return false because it will check for the whole word and the string should be end there
        main = self.root
        for char in word:
            if char not in main.children:
                return False
            else:
                main = main.children[char]
        return main.endhere
        
    def start_with(self,word):
        # start_with return true for ab in word abc or abcd
        main=self.root
        for char in word:
            if char not in main.children:
                return False
            else:
                main=main.children[char]
        return True
        
obj = Trie(None)
obj.insert("abcd")
obj.insert("apple")
obj.insert("banana")
obj.insert("pineapple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.start_with("app"))
        
