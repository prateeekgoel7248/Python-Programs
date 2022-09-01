class Solution(object):
    def validateStackSequences(self, pushed, popped):
        i = j = 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i - 1, j + 1
            i += 1
        return i == 0
        
/*
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
*/