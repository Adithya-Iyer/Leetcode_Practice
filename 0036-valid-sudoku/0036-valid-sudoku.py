class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowset, colset = set(), set()
            for j in range(9):
                rn = board[i][j]
                if rn.isdigit():
                    n = int(rn)
                    if n<1 or n>9 or n in rowset:
                        return False
                    rowset.add(n)
                cn = board[j][i]
                if cn.isdigit():
                    n = int(cn)
                    if n<1 or n>9 or n in colset:
                        return False
                    colset.add(n)
            if i%3==0:
                for j in range(0,9,3):
                    box = set()
                    for ii in range(3):
                        for jj in range(3):
                            bn = board[i+ii][j+jj]
                            if bn.isdigit():
                                n = int(bn)
                                if n<1 or n>9 or n in box:
                                    return False
                                box.add(n)
        return True