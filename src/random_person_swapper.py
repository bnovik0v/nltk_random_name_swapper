import re
import nltk
from nltk.tag import StanfordNERTagger
import numpy as np


class RandomPersonSwapper:
    def __init__(self):
        self.stanford_jar_path = 'stanford-corenlp/stanford-ner-4.2.0.jar'
        self.stanford_model_path = 'stanford-corenlp/classifiers/english.all.3class.distsim.crf.ser.gz'

        self.ner_tagger = StanfordNERTagger(self.stanford_model_path,
                                            self.stanford_jar_path,
                                            encoding='utf8')

    def __get_persons(self, text):
        words = nltk.word_tokenize(text)
        tagged_words = self.ner_tagger.tag(words)

        persons = []
        is_last_person = False

        for entity, tag in tagged_words:
            if tag == 'PERSON':
                if is_last_person == False:
                    persons.append(entity)
                else:
                    persons[-1] = persons[-1] + ' ' + entity
                is_last_person = True
            else:
                is_last_person = False

        return persons

    def __make_pairs(self, persons):
        max_n_rules = len(persons) // 2
        n_rules = np.random.randint(max_n_rules + 1)

        np.random.shuffle(persons)

        pairs = [[persons[i * 2], persons[i * 2 + 1]] for i in range(n_rules)]

        return pairs

    def __swap_persons(self, text, pairs):
        for pair in pairs:
            text = re.sub(rf'{pair[0]}|{pair[1]}',
                              lambda m: pair[0] if m.group() == pair[1] else pair[1], text)

        return text

    def make_replacement(self, text):
        persons = self.__get_persons(text)
        pairs = self.__make_pairs(persons)
        new_text = self.__swap_persons(text, pairs)

        return new_text, pairs