class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        q = Deque([(beginWord,0)])
        seen = set()
        
        while q:
            # print(q)
            curr, level = q.pop()
            if curr == endWord:
                return level+1
            if curr in seen:
                continue
            seen.add(curr)
            level += 1
            for i in range(len(curr)):
                options = [curr[0:i] + c + curr[i+1:] for c in "abcdefghijklmnopqrstuvwxyz" if c!=curr[i]]
                for option in options:
                    if option in wordset and option not in seen:
                        q.appendleft((option,level))
        return 0