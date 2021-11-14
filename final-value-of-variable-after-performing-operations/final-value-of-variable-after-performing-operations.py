class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        Better thought approach:
            
            iterate through list and check if '+' in operation, and add/subtract accordingly
            Time: 28 ms (86.84%), Space: 14 MB (91.43%) 
        """
        var = 0
        for op in operations:
            if '+' in op:
                var += 1
            else: 
                var -= 1
        return var
        
        
        """
        Rookie approach:
        
            Use dictionary and iterate array to decide which operation to apply to var  
            Time: 56 ms (44.33%), Space: 14.5 MB (17.05%) - LeetHub
        """
#         opDict = {
#             0 : '++X',
#             1 : 'X++',
#             2 : '--X',
#             3 : 'X--'
#         }
#         var = 0
#         for i in operations:
#             print(i)
#             if i == opDict[0]:
#                 var += 1
#             elif i == opDict[1]:
#                 var += 1
#             elif i == opDict[2]:
#                 var -= 1
#             elif i == opDict[3]:
#                 var -= 1
                
#         return var
                
