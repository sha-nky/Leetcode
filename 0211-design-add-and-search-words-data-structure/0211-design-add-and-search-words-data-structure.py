class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if i == len(word):
                return node.isEnd
            
            char = word[i]

            if char != ".":
                if char not in node.children:
                    return False
                node = node.children[char]
                return dfs(i+1, node)
            
            for ch in node.children.values():
                if dfs(i+1, ch):
                    return True
            
            return False
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)