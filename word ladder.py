#here we are just using a simple graph bfs(queue- breast first search), dfs will not work in graph for finding the shortest path because graph contain many unique paths unlike trees. 
# here we use a word and change its character to get the next character and it is just simple thing we are doing.....

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s=set(wordList)
        if endWord not in wordList:
            return 0
        q=[]
        q.append(beginWord)
        depth=0
        while q:
            depth+=1
            for l in range(len(q)):
                curr =q.pop(0)
                for i in range(len(curr)):
                    temp=[i for i in curr]
                    for c in range(97,123):
                        char = chr(c)
                        temp[i]=char
                        word=''.join(temp)
                        if curr==word:
                            continue
                        if word==endWord:
                            return depth+1
                        if word in s:
                            q.append(word)
                            s.remove(word)
        return 0


#much more concise code
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0