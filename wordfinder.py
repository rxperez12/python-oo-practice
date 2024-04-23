import random

PRACTICE_FILE_DIRECTORY = 'example2.txt'


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """ Takes in file path and reads file into an array. Prints number of
        words in file
        """

        self.file_path = file_path
        self.file_words = self.__read_file__()
        self.__repr__()

    def __read_file__(self):
        """Reads file and returns array of words"""
        file_data = open(self.file_path, 'r')
        return [word.strip() for word in file_data]

    def __repr__(self):
        print(f'{len(self.file_words)} words read')

    def random(self):
        """Returns random word from file_data"""
        return random.choice(self.file_words)


class SpecialWordFinder(WordFinder):
    """ Special Word Finder: finds random words from a file even including those
    with invalid lines."""

    # def __init__(self, file_path):
    #     """ Takes in file path and reads file into an array. Prints out words
    #     read"""

    #     super().__init__(file_path)
    #     self.file_words = self.__read_file__()

    def __read_file__(self):
        """Read file adds it to self.file_data. Disregards invalid lines"""
        words_with_invalid = super().__read_file__()
        return [word for word in words_with_invalid if word.isalpha()]


wf = WordFinder('example2.txt')
print(wf.random())
print(wf.random())


swf = SpecialWordFinder('example2.txt')
print(swf.random())
print(swf.random())
