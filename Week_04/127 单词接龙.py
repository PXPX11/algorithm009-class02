from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(endWord)):
                d[word[:i] + '*' + word[i+1:]].append(word)
        visited = set()
        queue = [(beginWord, 1)]
        while queue:
            current, step = queue.pop(0)
            visited.add(beginWord)
            for i in range(len(endWord)):
                inter = current[:i] +'*'+current[i+1:]
                for word in d[inter]:
                    if word == endWord:
                        return step +1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, step+1))
                d[inter] = []
        return 0