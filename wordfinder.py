"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    def __init__(self, words.txt):
        """Read dictionary and reports number of words"""
        
        dict_file = open(words.txt)
        self.words = self.parse(words) 
        print(f"{len(self.words)} words read")
    
    def parse(self, words):  
        """Parse dict_file -> list of words"""
        
        return [w.strip() for w in words]
    
    def random(self):
        return random.choice(self.words)
