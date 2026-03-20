class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # brute force solution 
        projects_st = []
        current_capital = w
        n = len(profits)
        projects_list = [[capital[i],profits[i]] for i in range(n)]
        projects_list.sort()
        i = 0
        while k:
            # pick the best project 
            best_profit = 0
            best_profit_i = None
            while i<n and projects_list[i][0]<=current_capital:
                heapq.heappush(projects_st, -projects_list[i][1])
                i+=1
            if len(projects_st)==0:
                break
            current_capital -= heapq.heappop(projects_st)
            k-=1
        return current_capital   