class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        # BFS visit
        curr_level = {beginWord}
        parents = collections.defaultdict(list)
        while curr_level:
            wordList -= curr_level
            #it is just an difference operator
            #like if we have two sets then it will remove the element which are in 2nd set and only those elements are remaining which is unique in set
            #ex- a[1,2,3,4,5]
            # b[4,5,6,7,8]
            #then a-b = [1,2,3] only 4,5 is removed because they are common
            next_level = set()
            for word in curr_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordList:
                            next_level.add(new_word)
                            parents[new_word].append(word)
            if endWord in next_level:
                #we are doing this because we want a shortest path if the endWord occured from any path and it occurs first time then it is the sortest path which we can get so we take this and we dont want any other paths because all others paths are greater than this path.
                break
            curr_level = next_level
        # DFS reconstruction
        res = []
        def dfs(word, path):
            if word == beginWord:
                path.append(word)
                res.append(path[::-1])
            else:
                for p_word in parents[word]:
                    dfs(p_word, path + [word])
        dfs(endWord, [])
        return res
        
        
        