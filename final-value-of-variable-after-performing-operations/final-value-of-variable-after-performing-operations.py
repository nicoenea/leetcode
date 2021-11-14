class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        
        """
        Rookie approach:
        
            Use dictionary and iterate array to decide which operation to apply to var
        """
        opDict = {
            0 : '++X',
            1 : 'X++',
            2 : '--X',
            3 : 'X--'
        }
        var = 0
        for i in operations:
            print(i)
            if i == opDict[0]:
                var += 1
            elif i == opDict[1]:
                var += 1
            elif i == opDict[2]:
                var -= 1
            elif i == opDict[3]:
                var -= 1
                
        return var
                