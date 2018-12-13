import unittest
import xmlrunner
import main


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.phrase = main.get_phrase()

    def test_size(self):
        # make sure the phrase has 5 words
        words = self.phrase.split(',')
        self.assertEqual(5, len(words))

    def test_buzz_words(self):
        # make sure there are 2 buzz words
        words = self.phrase.split(',')
        print(words)
        count_buzz = len(set(words).intersection(set(main.buzz)))
        print(count_buzz)
        self.assertEqual(2, count_buzz)

    def test_adjectives_words(self):
        # make sure there are 2 buzz words
        words = self.phrase.split(',')
        count_adjectives = len(set(words).intersection(set(main.adjectives)))
        self.assertEqual(1, count_adjectives)

    def test_adverbs_words(self):
        # make sure there are 2 buzz words
        words = self.phrase.split(',')
        count_adverbs = len(set(words).intersection(set(main.adverbs)))
        self.assertEqual(1, count_adverbs)

    def test_verbs_words(self):
        # make sure there are 2 buzz words
        words = self.phrase.split(',')
        count_verbs = len(set(words).intersection(set(main.verbs)))
        self.assertEqual(1, count_verbs)

