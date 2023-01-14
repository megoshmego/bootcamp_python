"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, path):
        """Read dictionary and reports number of words"""
    
        dict_file = open(path)
        self.words = self.parse("megoshmego/bootcamp_python/words.txt", "r") 
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):  
        """Parse dict_file -> list of words"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word."""
        
        return random.choice(self.words)
