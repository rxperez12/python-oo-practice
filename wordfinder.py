import random

PRACTICE_FILE_DIRECTORY = 'example.txt'


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """Create model for word finder - Finds a random word in a given file
        provided file has one word per line
        """

        self.file_path = file_path
        self.file_data = []
        self.word_counter = None
        self.__read_file__()

    def __read_file__(self):
        """Read file adds it to self.file_data. Populates word_counter and prints
        how many words were read"""
        file_data = open(self.file_path, 'r')
        counter = 0
        for word in file_data:
            self.file_data.append(word.replace('\n', ''))
            counter += 1
        self.word_counter = counter
        self.__repr__()

    def __repr__(self):
        print(f'{self.word_counter} words read')

    def random(self):
        """Returns random word from file_data"""
        return random.choice(self.file_data)


wf = WordFinder(PRACTICE_FILE_DIRECTORY)

print(wf.random())
print(wf.random())
print(wf.random())
