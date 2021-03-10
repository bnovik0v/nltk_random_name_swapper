# nltk library
import nltk
from nltk.tag import StanfordNERTagger

# additional libraries
import numpy as np
import re


class RandomPersonSwapper:
    """ RandomPersonSwapper make random swaps in text

    Methods
    -------
    make_swapping(text)
        make random swaps in text
    """

    def __init__(self):
        # set StanfordNERTagger files paths
        self.stanford_jar_path = './stanford-corenlp/stanford-ner-4.2.0.jar'
        self.stanford_model_path = './stanford-corenlp/classifiers/english.all.3class.distsim.crf.ser.gz'

        # init StanfordNERTagger model
        self.ner_tagger = StanfordNERTagger(self.stanford_model_path,
                                            self.stanford_jar_path,
                                            encoding='utf8')

    def __get_persons_from_text(self, text):
        """ Extract persons from text

        :param text: text
        :return: persons
        """

        # Get tagged words from text
        words = nltk.word_tokenize(text)
        tagged_words = self.ner_tagger.tag(words)

        # Gather names that consist of few words
        # e.g. ['Mike', 'Pearson'] -> ['Mike Pearson']
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

    def __make_rules_from_persons(self, persons):
        """ Make random rules from persons list

        :param persons: list of persons
        :return: return random rules
        """

        # Set number of rules (half of the number of persons)
        n_rules = len(persons) // 2

        # Shuffle persons list
        np.random.shuffle(persons)

        # Gather pairs (rules) from persons list
        rules = [[persons[i * 2], persons[i * 2 + 1]] for i in range(n_rules)]

        return rules

    def __swap_persons_in_text(self, text, rules):
        """ Swap persons in text using rules

        :param text: text
        :param rules: rules
        :return: text with swaps
        """

        for pair in rules:
            text = re.sub(rf'{pair[0]}|{pair[1]}',
                          lambda m: pair[0] if m.group() == pair[1] else pair[1], text)

        return text

    def make_swapping(self, text):
        """ Make random person swaps in text

        :param text: text
        :returns: text with random swaps and rules (e.g. Person2 <-> Person5)
        """

        persons = self.__get_persons_from_text(text)
        rules = self.__make_rules_from_persons(persons)
        new_text = self.__swap_persons_in_text(text, rules)

        return new_text, rules
