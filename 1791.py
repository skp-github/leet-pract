class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_1, edge_2 = edges[0][0], edges[0][1]
        if edge_1 not in edges[1] or edge_1 not in edges[1]:
            return edge_2
        else:
            return edge_1


# not a good question straight forward question
