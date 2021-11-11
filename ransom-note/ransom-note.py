class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        First Approach:
        
            1. Hold all matching values in a list
            2. Iterate and check if chars in ransomNote are in magazine
            3. if there are enough values to complete the ransomNote, append them to our hold list
            4. Make sure to account for single values
            5. If more than one value in ransomNote, use count to append values to hold
        """
        holder = [] # 1
        for char in ransomNote:
            if char in magazine: #2
                if magazine.count(char) >= ransomNote.count(char): #3
                    if ransomNote.count(char) == 1: # 4
                        holder.append(char)
                    else:
                        if holder.count(char) < ransomNote.count(char):
                            print("Wtf", holder.count(char))
                            for amount in range(0,ransomNote.count(char)): # 5
                                holder.append(char)
        print(holder)
        if len(holder) == len(ransomNote):
            return True
        else:
            return False