class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        row, col = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            nextNode = node.children[char]
            if nextNode.word:
                res.append(nextNode.word)
                nextNode.word = None
            
            board[r][c] = "#"
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != "#":
                    dfs(nr, nc, nextNode)
            board[r][c] = char
        
        for r in range(row):
            for c in range(col):
                dfs(r, c, trie.root)
        return res
