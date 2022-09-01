class Solution(object):
    def wordSubsets(self, A, B):
        result = []
        subsetLetters = {}
        for word in B: #word represent e, oo
        	for letter in word: #letter represent each alphabet
                #create dict for alphabet
        		if letter not in subsetLetters:
        			subsetLetters[letter] = word.count(letter) 
        		else:
        			subsetLetters[letter] = max(word.count(letter),subsetLetters[letter])
        print(subsetLetters)
        for word in A:
        	if all(subsetLetters[letter]<=word.count(letter) for letter in subsetLetters):
        		result.append(word)
        return result
        # count = collections.Counter()
        # for b in B:
        #     count |= collections.Counter(b)
        # return [a for a in A if not count - Counter(a)]