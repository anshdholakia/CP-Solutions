class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        column_to_walls = {}
        total_columns = sum(wall[0])
        for row in range(len(wall)):
            cur_sum=0
            for brick in wall[row][:-1]:
                cur_sum+=brick
                column_to_walls[cur_sum]=column_to_walls.get(cur_sum, 0)+1
        return len(wall)-max(column_to_walls.values()) if column_to_walls else len(wall)