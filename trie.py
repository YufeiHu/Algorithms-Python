from collections import defaultdict


class trie_node(object):

    def __init__(self):
        self.children = defaultdict(trie_node)
        self.is_word = False


class trie(object):

    def __init__(self):
        self.root = trie_node()

    def insert(self, word):
        ptr = self.root
        for char in word:
            ptr = ptr.children[char]
        ptr.is_word = True

    def search(self, word):
        ptr = self.root
        for char in word:
            ptr = ptr.children.get(char)
            if not ptr:
                return False
        return ptr.is_word

    def starts_with(self, prefix):
        ptr = self.root
        for char in prefix:
            ptr = ptr.children.get(char)
            if not ptr:
                return False
        return True


if __name__ == "__main__":
    trie_inst = trie()

    trie_inst.insert("apple")
    print(trie_inst.search("apple"))
    print(trie_inst.search("app"))
    print(trie_inst.starts_with("app"))

    trie_inst.insert("app")
    print(trie_inst.search("app"))
