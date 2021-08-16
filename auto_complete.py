class AutoCompleteData:
    def __init__(self, sentence, src_txt, offset, score):
        self.completed_sentence = sentence
        self.source_text = src_txt
        self.offset = offset
        self.score = score

    def __str__(self):
        return f'Auto[sen:{self.completed_sentence}, src:{self.source_text}, ofst: {self.offset}, score:{self.score}]'

    def __repr__(self):
        return f'Auto[sen:{self.completed_sentence}, src:{self.source_text}, ofst: {self.offset}, score:{self.score}]'

    def get_sentence(self):
        return self.completed_sentence

    def get_src(self):
        return self.source_text

    def get_score(self):
        return self.score

    def get_offset(self):
        return self.offset
