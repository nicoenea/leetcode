class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        dic_words = {}
        for word in words:
            newword = ''.join(sorted(list(set(list(word)))))
            dic_words[newword] = dic_words.setdefault(newword,0) + 1
        res = []
        for puzzle in puzzles:
            count = 0
            first = puzzle[0]
            puzzle = ''.join(sorted(list(set(list(puzzle[1:])))))
            if puzzle.find(first) != -1:
                inx = puzzle.find(first)
                puzzle = puzzle[:inx] + puzzle[inx+1:]
            if first in dic_words:
                count += dic_words[first]
            queue = []
            for (i,v) in enumerate(puzzle):
                queue.append((v,i))
            while len(queue) > 0:
                v,i = queue.pop(0)
                if i == len(puzzle) - 1:
                    key = ''.join(sorted(list(first + v)))
                    if key in dic_words:
                        count += dic_words[key]
                    continue
                queue.append((v,i+1))
                queue.append((v + puzzle[i+1],i+1))
            res.append(count)
        return res
                            
                    