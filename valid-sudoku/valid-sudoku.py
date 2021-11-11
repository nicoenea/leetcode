class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        
        '''three hash maps for checking condition'''
        check_dict_x ={}
        check_dict_y = {}
        check_dict_box = {}
        
        '''initializing hasmaps to empty lists for 9 rows and 9 columns'''
        for i in range(9):
            check_dict_x[i] = []
            check_dict_y[i] = []
        
        """initializing hashmaps to empty lists for 9 boxes
        (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)"""
        for i in range(3):
            for j in range(3):
                check_dict_box[(i,j)] = []

        # iterating through all elements
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    '''check existance of current element in previous ones'''
                    if board[i][j] not in check_dict_x[i]:
                        '''if not then add them to list'''
                        check_dict_x[i].append(board[i][j])
                    else:
                        return False
                    '''integer division by 3 of coordinates to map boxes to coordinates
                    eg: (6//2, 6//2) to (8//3, 8//3) -> (2,2)'''
                    if board[i][j] not in check_dict_box[(i//3,j//3)]: 
                        check_dict_box[(i//3,j//3)].append(board[i][j])
                    else:
                        return False
                if board[j][i] != '.':
                    '''check existance of current element in previous ones'''
                    if board[j][i] not in check_dict_y[i] or board[j][i] == '.':
                        '''if not then add them to list'''
                        check_dict_y[i].append(board[j][i])
                    else:
                        return False

        return True