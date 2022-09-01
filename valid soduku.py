class Solution(object):
    def isValidSudoku(self, board):
        # board=list(map(str,board))
        seen=set()
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if ('r'+str(i)+board[i][j]) in seen or ('c'+str(j)+board[i][j]) in seen or (('b'+str((i//3)*3+(j//3)))+board[i][j]) in seen:
                        return False
                    else:
                        seen.add('r'+str(i)+board[i][j])
                        seen.add('c'+str(j)+board[i][j])
                        seen.add(('b'+str((i//3)*3+(j//3)))+board[i][j])
        return True
                        
                
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        