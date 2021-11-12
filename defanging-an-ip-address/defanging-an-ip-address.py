class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        # use replace() function
        
        address = address.replace('.', '[.]')
        
        return address