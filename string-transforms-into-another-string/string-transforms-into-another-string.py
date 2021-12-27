class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        conversion_map = dict()
        unique_in_str2 = set()
        
        # Make sure that no char in str1 is mapped to multiple chars in str2
        for letter1, letter2 in zip(str1, str2):
            if letter1 not in conversion_map:
                conversion_map[letter1] = letter2
                unique_in_str2.add(letter2)
            elif conversion_map[letter1] != letter2:
                # letter1 maps to 2 diff chars, so str1 cannot transform into str2
                return False
            
        if len(unique_in_str2) < 26:
            # no char in str1 maps to 2 or more diff chars in str2, and ther is
            # at least one temp char that can be used to break any loop
            return True
        
        # The conversion map forms one or more cycles, and there are no temp chars
        # that we can use to break the loops, so str1 cannot transform into str2
        return False