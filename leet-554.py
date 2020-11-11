class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}
        for layer in wall:
            length = 0
            for brick in range(0, len(layer) - 1):
                length += layer[brick]
                edges[length] = edges.get(length, 0) + 1
        if not edges.keys(): return len(wall)
        return len(wall) - (max(edges.values()))
            