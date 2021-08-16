# passes at the trie with the word, and return the trie where finished if word exists, else None
def look_for_seq(seq, root):
    node = root
    for char in seq:
        if node.get_children().get(char):
            node = node.get_children()[char]
        else:
            return None
    return node


# returns the array of sentences which begin with prefix
def query(trie, prefix):
    res = []
    node = look_for_seq(prefix, trie.get_root())
    if not node:
        return res
    trie.dfs(node, prefix, res)
    # res = [[word, len(prefix)] for word in res]
    return res


def query_whole_word(trie, prefix):
    return [[word, len(prefix)] for word in query(trie, prefix)]


# looks for word with one absent word, returns array of sentenced contains such words
def query_abs_char(trie, word):
    res_words = []
    for i in range(len(word)):
        score = len(word) - (10 - i * 2) if len(word) < 4 else len(word) - 2
        find_words = query(trie, word[:i]+word[i+1:])
        res_words += [[word, score] for word in find_words]
    return res_words


# looks for words with one replaced char, returns array of sentenced contains such words
def query_rep_char(trie, word):
    res_words, temp_words = [], []
    for i in range(len(word)):
        next_node= look_for_seq(word[:i], trie.get_root())
        score = len(word)-(5-i) if i < 4 else len(word)-1
        if next_node:  # skips the replaced node
            for rep_key, rep_val in next_node.get_children().items():
                next_node = look_for_seq(word[i+1:], rep_val)
                # if the word was found then adds all of sentences which contains the word
                if next_node and rep_key != word[i]:
                    trie.dfs(next_node, word[:i]+rep_key+word[i+1:], temp_words)
                    res_words += [[word, score] for word in temp_words]
    return res_words


# looks for words with one added char, returns array of sentenced contains such words
def query_add_char(trie, word):
    res_words, temp_words = [], []
    for i in range(1, len(word)+1):
        score = len(word) - (10 - i * 2) if len(word) < 4 else len(word) - 2
        next_node = look_for_seq(word[:i], trie.get_root())
        if next_node:  # adds the added node
            for add_node_key, add_node_val in next_node.get_children().items():
                next_node = look_for_seq(word[i:], add_node_val)
                if next_node:  # if the word was found then adds all of sentences which contains the word
                    trie.dfs(next_node, word[:i] + add_node_key + word[i:], temp_words)
                    res_words += [[word, score] for word in temp_words]
    return res_words
