# 208. Implement Trie (Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

#solution referenced from https://leetcode.com/problems/implement-trie-prefix-tree/discuss/774379/Python-Solution-with-Explanation

class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isWordEnd = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currnode = self.root
        for ch in word:
            node = currnode.childNodes.get(ch, TrieNode())
            currnode.childNodes[ch] = node
            currnode = node
        
        currnode.isWordEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currnode = self.root
        for ch in word:
            node = currnode.childNodes.get(ch)
            if not node:
                return False
            currnode = node
        
        return currnode.isWordEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currnode = self.root
        for ch in prefix:
            node = currnode.childNodes.get(ch)
            if not node:
                return False
            currnode = node
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)