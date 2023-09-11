from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:  # if k is 0, return the original string
            return s
        pq = [(-freq, key) for key, freq in Counter(s).items()] 
        heapq.heapify(pq)
        waitlist = deque()
        res = ""
        
        while pq:
            freq, key = heapq.heappop(pq)  
            res += key
            waitlist.append((freq+1, key))  
            
            if len(waitlist) < k:  
                continue
            
           
            freq, key = waitlist.popleft()
            if freq < 0:
                heapq.heappush(pq, (freq, key))

        
        while waitlist:
            freq, key = waitlist.popleft()
            if freq < 0: 
                return ""
        
        return res 