from json import JSONEncoder


class TrieNode(JSONEncoder):
    def __init__(self):
        super().__init__()
        self.__ind = []
        self.__children = {}

    def set_ind(self, ind):
        self.__ind.append(ind)

    def add_child(self, child):
        self.__children.update(child)

    def get_ind(self):
        return self.__ind

    def is_end(self):
        return self.get_children() == {}

    def get_children(self):
        return self.__children

    def __str__(self):
        return str(self.__children) + str(self.__ind)

    def __repr__(self):
        return str(self.__children) + str(self.__ind)


class Trie:
    def __init__(self):
        self.__root = TrieNode()

    def get_root(self):
        return self.__root

    def set_root(self, new_root):
        self.__root = new_root

    # gets a sentence and insert into the trie all of cons sub sequences inside the sentence
    def insert_seq(self, sentence, ind):
        for i in range(len(sentence)):
            self.insert(sentence[i:], ind)

    # insert the sequence into the trie
    def insert(self, short_seq, ind):
        node = self.get_root()
        sentence_len = len(short_seq)
        for i in range(len(short_seq)):
            next_node = node.get_children().get(short_seq[i])
            if next_node is None:
                new_node = TrieNode()
                node.add_child({short_seq[i]: new_node})
                node = new_node
            else:
                node = next_node
            if i == sentence_len - 1:
                node.set_ind(ind)

    def __str__(self):
        return str(self.get_root().get_children())

    def __repr__(self):
        return str(self.get_root().get_children())

    # passes at the trie and collect all of string to res array
    def dfs(self, node, prefix, res):
        if node.is_end():
            for i in node.get_ind():
                if i not in res:
                    res.append(i)
        for key, value in node.get_children().items():
            self.dfs(value, prefix + key, res)

