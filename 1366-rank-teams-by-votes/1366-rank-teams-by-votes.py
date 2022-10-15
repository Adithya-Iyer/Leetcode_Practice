class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        l = len(votes)
        if l==1:
            return votes[0]
        teams = list(votes[0])
        teams.sort()
        t = len(teams)
        rank = [{teams[i]: 0 for i in range(t)} for j in range(t)]
        for v in votes:
            for i,p in enumerate(v):
                rank[i][p] += 1
        print(rank)
        def getTeams(ind, pre):
            ret = []
            if len(pre)==1 or ind==t:
                return pre[0]
            cnt = 0
            for pt in pre:
                if rank[ind][pt] > cnt:
                    cnt = rank[ind][pt]
                    ret = [pt]
                elif rank[ind][pt] == cnt:
                    ret.append(pt)
            return getTeams(ind+1, ret)
        answer = []
        for i in range(t):
            ans = getTeams(0, teams)
            answer.append(ans)
            teams.remove(ans)
        return ''.join(answer)