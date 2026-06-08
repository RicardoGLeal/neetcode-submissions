class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.is_end = False  # marks end of a valid word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            # create node for this char if it doesn't exist yet
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        # mark the final node as a complete word
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                ch = word[j]

                if ch == ".":
                    # wildcard: try every possible child and recurse from next index
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    # no child path led to a valid word
                    return False

                elif ch not in curr.children:
                    # literal char not found — dead end
                    return False

                # advance to the next node
                curr = curr.children[ch]

            # consumed all chars — valid only if we're at a word boundary
            return curr.is_end

        return dfs(0, self.root)