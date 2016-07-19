
class KanaMap:
    """ Represents a Mapping of Kana to Roman Characters """
    
    def __init__(self, normalMapping, consonants, *, iChars, yMappings, doubleChar):
        """ Initialize with any normal Mappings the Mapping of all consonant characters that can be doubled, 
            the characters that end in i sounds, the y Character Mappings and the double COnsonant Character """
        self.normalMapping = normalMapping
        self.doubleChar = doubleChar
        
        self.compoundMapping = {key+yKana:consonants[key][:-1]+yKanaValue for key in iChars for yKana, yKanaValue in yMappings.items()}
        self.doubleConsonantMapping = {doubleChar+key:value[0]+key for key, value in consonants.items()}
        self.normalMapping.update(consonants)
        
    def getMappings(self, symbols):
        """ Return the Mappings to use given the symbols that should not be converted """
        maps = [self.doubleConsonantMapping] if self.doubleChar not in symbols else []
        maps.extend([self._process_mapping(self.compoundMapping, symbols),
                     self._process_mapping(self.normalMapping, symbols)])
        return maps

    def _process_mapping(self, mapping, symbols):
        """ Return the proper mapping dictionary that will not convert the learned symbols """
        return {key:value for key, value in mapping.items() if not set(key).issubset(symbols)}