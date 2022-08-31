import heapq

def minimumEffortPath(heights):
    """
    :type heights: List[List[int]]
    :rtype: int
    """

    if not 8 % 2:
        print('hello')

    m,n = len(heights),len(heights[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    output = 0
    heap = [(0,0,0)]
    visited = set()
    while heap:
        for h in heap:
            print(h)
        print()
        k,x,y = heapq.heappop(heap)
        print('popped ({}, {}, {})'.format(k,x,y))
        print('========================')
        output = max(output,k)
        if (x,y) == (m-1,n-1):
            return output
        visited.add((x,y))
        for dx, dy in dirs:
            new_x,new_y = x+dx,y+dy
            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                new_k = abs(heights[x][y]-heights[new_x][new_y])
                heapq.heappush(heap,(new_k,new_x,new_y))
    return -1

heights = [[1,2,3],[2,5,1],[6,2,1]]
print(minimumEffortPath(heights))