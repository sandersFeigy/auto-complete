def filter_chars(word):
    word = ' '.join(word.split())  # leaves no multiple ' '
    # remove numeric, uppercase and special chars
    return ''.join([char.lower() for char in word if (char.isalnum() or char == ' ') and not char.isnumeric()])


def select_high_score(popular_words):
    highest = list(popular_words.values())[:5]
    highest.sort(key=lambda item: (item.get_score()*-1, item.get_sentence()))  # the -1* is in order to make descending order of scores
    return highest


# Gets file path and return its content
def get_file_content(file):
    try:
        with open(file, "r", encoding="utf8") as f:
            file = f.readlines()
        f.close()
        return file
    except Exception as exp:
        print(exp)


