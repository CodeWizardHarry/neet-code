""""

This version changes neetcode's find function to a recursive one,
because i think the recursive version is easier to understand

Useful links:
    https://www.youtube.com/watch?v=ayW5B2W9hfo&ab_channel=PotatoCoders
    https://www.youtube.com/watch?v=gKKATlgNNqM&ab_channel=HappyCoding
    
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            # res is the root/parent node
            if n != par[n]:
                par[n] = find(par[n]) #path compression
                return par[n]     
            else:
                return n           
                
            
        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1,n2)
        return res
        

        # Recursive implementation of the find function
        # def find(n):
        #     p = par[n]
        #     while p != par[p]:
        #         par[p] = par[par[p]]
        #         p = par[p]
        #     return p