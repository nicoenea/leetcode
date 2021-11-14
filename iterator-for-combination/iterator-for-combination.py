class CombinationIterator:
    
    """
    Easy Approach using combinations from itertools:
    
        1. Store all possible combinations in self.allCombinations, by using the itertools function 'combinations()' 
                this function will return all the possible combinations in a list/string, given the desired length of the combinations ( combinationLength )
        1b. We take 'characters' and 'combinationLength' to get all possible combinations in the string 'characters', and then put all the possible combinations in a list.
        
        2. next returns the next combination given the length, so we use a counter to change to the next combination (this can be simplified to one line)
        
        3. If self.count is less than the amount of combinations, we return True to show that there are still possible combinations left to show.
    """

    def __init__(self, characters: str, combinationLength: int):
        self.allCombinations  = list(itertools.combinations(characters, combinationLength)) # 1
        self.count = 0
        print(self.allCombinations)

    def next(self) -> str:
        string = ''.join(self.allCombinations[self.count]) # 2 
        self.count += 1
        return string
        

    def hasNext(self) -> bool:
        
        if self.count < len(self.allCombinations): # 3
            return True
        else:
            return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()