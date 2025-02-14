#211. Design Add and Search Words Data Structure

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, word):
        def dfs(j, root):
            current = root
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.is_end_of_word
        return dfs(0, self.root)