class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Attempt 1 - 48/53 test cases passed
        # rows = {
        #     2: set(), 3: set(), 4: set(), 5: set(),
        #     6: set(), 7: set(), 8: set(), 9: set()
        # }
        # for row,seat in reservedSeats:
        #     if 1<seat and seat<10:
        #         rows[seat].add(row)
        # groups = 0
        # for i in range(1, n+1):
        #     left4 = (i not in rows[2]) and (i not in rows[3]) and (i not in rows[4]) and (i not in rows[5])
        #     right4 = (i not in rows[6]) and (i not in rows[7]) and (i not in rows[8]) and (i not in rows[9])
        #     if left4 and right4:
        #         groups += 2
        #     else:
        #         center = (i not in rows[4]) and (i not in rows[5]) and (i not in rows[6]) and (i not in rows[7])
        #         if left4 or center or right4:
        #             groups += 1
        # return groups
        #
        # Attempt 2
        gone = set()
        resrows = set()
        for row,seat in reservedSeats:
            resrows.add(row)
            lg, cg, rg = str(row)+'L', str(row)+'C', str(row)+'R'
            left = (seat>1 and seat<6) and (lg not in gone)
            right = (seat>5 and seat<10) and (rg not in gone)
            center = (seat>3 and seat<8) and (cg not in gone)
            if left:
                gone.add(lg)
            if center:
                gone.add(cg)
            if right:
                gone.add(rg)
        groups = (n - len(resrows)) * 2
        for row in resrows:
            lg, cg, rg = str(row)+'L', str(row)+'C', str(row)+'R'
            if (lg not in gone) and (rg not in gone):
                groups += 2
            elif (lg not in gone) or (cg not in gone) or (rg not in gone):
                groups += 1
        return groups