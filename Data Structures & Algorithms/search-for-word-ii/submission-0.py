class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        self.createTrie(words)

        def dfs(r, c, node, visited):
            # return when outside of bounds.
            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return
            
            # return when cel already visited in current path
            if (r, c) in visited:
                return
            
            visited.add((r,c))

            # return when cel letter not in node children
            if board[r][c] not in node.children:
                visited.remove((r,c))
                return
            
            # move node
            node = node.children[board[r][c]]

            # word found, add to res
            if node.word != None:
                res.append(node.word)
                node.word = None
                 
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for i, j in dirs:
                dfs(r+i, c+j, node, visited)

            visited.remove((r,c))
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, self.root, set())
        return res

    def createTrie(self, words):
        self.root = TrieNode()

        for word in words:
            self.insertWord(word)

    def insertWord(self, word):
        node = self.root

        for ch in word: 
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

    

        
        

        