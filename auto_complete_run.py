from auto_complete import AutoCompleteData
from create_db import CreateDB
from func_find_wrong_words import query_abs_char, query_add_char, query_rep_char, query_whole_word


class RunAutoComp:
    def __init__(self, path):
        self.__trie = CreateDB()
        self.__path = path

    def get_trie(self):
        return self.__trie

    def initialize(self):  # unchecked func
        self.__trie.create_db(self.__path)

    def completion(self, word):
        reg_words = query_whole_word(self.__trie.get_database(), word)
        del_words = query_abs_char(self.__trie.get_database(), word)
        add_words = query_add_char(self.__trie.get_database(), word)
        rep_words = query_rep_char(self.__trie.get_database(), word)
        all_words = reg_words + del_words + add_words + rep_words
        all_words.sort(key=lambda cur_word: cur_word[1] * -1)  # the -1* is in order to make descending order of scores
        popular_words = {}
        for word_item in all_words:
            word_info = self.__trie.get_auto_complete().get(
                word_item[0])  # gets the details info which connected to word
            if not popular_words.get(word_info[0]):  # ignore next words which contain current word
                popular_words.update({word_info[0]: AutoCompleteData(word_info[0], word_info[1],
                                                                     word_info[0].lower().find(word), word_item[1])})
        return popular_words
