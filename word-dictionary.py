class TrieNode:
    def __init__(self):
        self.childnodes = {}
        self.isWordEnd = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currnode = self.root
        for ch in word:
            node = currnode.childnodes.get(ch,TrieNode())
            currnode.childnodes[ch] = node
            currnode = node
        
        currnode.isWordEnd = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word == "":
            return False
        else:
            return searchArray([x for x in word], ,0, self.root)
        
    def searchArray(self, array, startpos, startnode):
        currnode = startnode
        for i in range(len(array)):
            if not curr:
                break
            else:
                if array[i] == ".":
                   print(currnode.childnodes.)
                   return [searchArray(array[i+1:],length,currnode.childnodes.get(ch)) for ch in current.childnodes]
            
                    
                
            
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)