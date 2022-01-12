class Node:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.isEnd = False  # 用来标记是否是当前trie分支的末尾

    def contain_key(self, ch):
        return self.child[ord(ch)-ord('a')]

    def get(self, ch):
        return self.child[ord(ch)-ord('a')]

    def put(self, ch):
        # 开始时每一层都是None，有字母放入时，将字母对应位置变为Node
        self.child[ord(ch)-ord('a')] = Node()


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # 指针指向初始位置
        p = self.root
        for i in word:
            # 如果不在trie中，将其放进去
            if not p.contain_key(i):
                p.put(i)
            # 指针指向当前node
            p = p.get(i)
        # 将末尾的None的标志参数isEnd变为True
        p.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for i in word:
            if not p.contain_key(i):
                return False
            else:
                p = p.get(i)
        # 如果字母都在trie中，返回最后一个字母的标志参数isEnd（是否是当前trie分支的末尾）
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for i in prefix:
            if not p.contain_key(i):
                return False
            else:
                p = p.get(i)
        # 与search不同，这里不需要判断是否是当前trie分支的末尾
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # 返回 True
    print(trie.search("app"))    # 返回 False
    print(trie.startsWith("app"))  # 返回 True
    trie.insert("app")
    print(trie.search("app"))  # 返回 True
