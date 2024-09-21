# copy over your a1_partd.py file here
from a1_partc import Queue

def get_overflow_list(grid, r=0, c=0, overflow_list=None):
    if overflow_list is None:
        overflow_list = []

 
    def count_surrounding_cells(row, col):
        return sum(
            1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0])
        )

    if r < len(grid):
        if c < len(grid[0]):
            count = count_surrounding_cells(r, c)

            if abs(grid[r][c]) >= count:
                overflow_list.append((r, c))

            get_overflow_list(grid, r, c + 1, overflow_list)
        else:

            get_overflow_list(grid, r + 1, 0, overflow_list)

    return overflow_list if overflow_list else None

def overflow(grid, a_queue, overflow_count=0):
    
    same_one = all(grid[i][j] >= 0 for i in range(len(grid)) for j in range(len(grid[0]))) or all(grid[i][j] <= 0 for i in range(len(grid)) for j in range(len(grid[0])))

    if same_one:
        return overflow_count
    
    overflow_list = get_overflow_list(grid)

    if not overflow_list:
        return overflow_count

    if grid[overflow_list[0][0]][overflow_list[0][1]] < 0:
        is_positive = False
    else:
        is_positive = True

    for i, j in overflow_list:
        grid[i][j] = 0
        
    for i, j in overflow_list:
        if i > 0 and is_positive:
            grid[i - 1][j] = abs(grid[i - 1][j]) + 1
        elif i > 0 and not is_positive:
            grid[i - 1][j] = -abs(grid[i - 1][j]) - 1

        if i < len(grid) - 1 and is_positive:
            grid[i + 1][j] = abs(grid[i + 1][j]) + 1
        elif i < len(grid) - 1 and not is_positive:
            grid[i + 1][j] = -abs(grid[i + 1][j]) - 1

        if j > 0 and is_positive:
            grid[i][j - 1] = abs(grid[i][j - 1]) + 1
        elif j > 0 and not is_positive:
            grid[i][j - 1] = -abs(grid[i][j - 1]) - 1

        if j < len(grid[0]) - 1 and is_positive:
            grid[i][j + 1] = abs(grid[i][j + 1]) + 1
        elif j < len(grid[0]) - 1 and not is_positive:
            grid[i][j + 1] = -abs(grid[i][j + 1]) - 1

    final_grid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    a_queue.enqueue(final_grid)

    return overflow(grid, a_queue, overflow_count + 1)
