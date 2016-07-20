from .symbols import HIRAGANA_MAP, KATAKANA_MAP

from cached_property import cached_property
from kao_symbols import convert

class RomKanConverter:
    """ Helper class to manage converting Japanese Character strings into a form the User can understand based on their Learned Symbols """
    
    def __init__(self, symbols):
        """ Initialize with the Symbols the User has learned """
        self.symbols = set(symbols)
        
    def convert(self, word):
        """ Convert the given Word """
        return convert(word, self.symbolMaps)
        
    @cached_property
    def symbolMaps(self):
        return HIRAGANA_MAP.getMappings(self.symbols) + KATAKANA_MAP.getMappings(self.symbols)
