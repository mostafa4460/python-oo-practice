from random import randint

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """ This class reads an on disk file containing words (1 per line) and provides different functionality 
    
    FUNCTIONS
        make_list_of_words: reads the file passed in and makes a list of all the words in it

        random: returns a random word from the list of words
    """

    def __init__(self, path):
        """ Opens a file, makes a list of all the words in it, then prints out the number of words """

        with open(path, "r") as file:
            self.words = self.make_list_of_words(file)

        print(f"{len(self.words)} words read")


    def make_list_of_words(self, file):
        """ Makes a list of all the words in a given file without the '\n' at the end of each word """

        words = []

        for line in file:
            newline_i = line.find('\n')
            if newline_i != -1:
                words.append(line[:newline_i])
            else:
                words.append(line)
        
        return words

    def random(self):
        """ Returns a random word from the list of words """
        
        return self.words[randint(0, len(self.words) - 1)]

class SpecialWordFinder(WordFinder):
    """ This class is a subclass of WordFinder but accounts for comments and empty lines """

    def __init__(self, path):
        """ Uses WordFinder initializer to open a file and make a list of all the words in it"""
        super().__init__(path)

    def make_list_of_words(self, file):
        """ Makes a list of all the words in a given file but redacts comments and empty lines """

        words = []

        for line in file:
            newline_i = line.find('\n')
            if newline_i != -1 and line[0] != '\n' and line[0] != "#":
                words.append(line[:newline_i])
            elif line[0] != '\n' and line[0] != "#":
                words.append(line)
        
        return words
