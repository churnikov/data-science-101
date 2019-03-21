from collections import Counter
from typing import Union, List, Callable


class Vocab:

    def __init__(self, vocab_size=1000):
        self.vocab_size = vocab_size
        self.counts: Counter = Counter()
        self.word2id = {}
        self.id2word = {}

    def __len__(self):
        return len(self.word2id)

    def count(self, text: Union[str, List[str], List[List[str]]]):
        if isinstance(text, str):
            self.counts[text] += 1
        elif isinstance(text, list) or isinstance(text, TextDataset):
            for t in text:
                self.count(t)
        else:
            raise TypeError('text should be either list of strings or string')

    def build_vocab(self, text: Union[str, List[str], List[List[str]]]):
        if type(self.counts) != dict:
            self.count(text)
            self.counts = dict(self.counts.most_common(self.vocab_size))
        if isinstance(text, str):
            if text in self.counts and text not in self.word2id:
                self.word2id[text] = len(self.id2word)
                self.id2word[self.word2id[text]] = text
        elif isinstance(text, list) or isinstance(text, TextDataset):
            for t in text:
                self.build_vocab(t)
        else:
            raise TypeError('text should be either list of strings or string')


class TextDataset:

    def __init__(self, data: Union[str, List[str]], preprocessor: Callable, vocab: Vocab=None):
        self.data_source = data
        self.preprocessor = preprocessor
        self.vocabulary = vocab

    def __iter__(self):
        if isinstance(self.data_source, str):
            with open(self.data_source, 'r') as f:
                for l in f:
                    if self.vocabulary is not None:
                        yield [t for t in self.preprocessor(l) if t in self.vocabulary.counts]
                    else:
                        yield self.preprocessor(l)
        elif isinstance(self.data_source, list):
            for l in self.data_source:
                yield self.preprocessor(l)
        else:
            raise TypeError('`data` should be either name of file or list examples')
