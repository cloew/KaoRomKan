from .symbols import HIRAGANA_MAP, COMPOUND_HIRAGANA_MAP, DOUBLE_CONS_HIRAGANA_MAP, DOUBLE_CONS_COMPOUND_HIRAGANA_MAP

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
        """ Return the maps of symbols that should be converted """
        maps = [self._process_mapping(DOUBLE_CONS_COMPOUND_HIRAGANA_MAP),
                self._process_mapping(DOUBLE_CONS_HIRAGANA_MAP),
                self._process_mapping(COMPOUND_HIRAGANA_MAP),
                self._process_mapping(HIRAGANA_MAP)]
        return maps

    def _process_mapping(self, mapping):
        """ Return the proper mapping dictionary that will not convert the learned symbols """
        return {key:value for key, value in mapping.items() if not set(key).issubset(self.symbols)}