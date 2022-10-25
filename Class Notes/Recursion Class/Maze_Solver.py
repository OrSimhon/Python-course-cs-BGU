# Recursion Class

def isValid(grid, neighbor):
    """
    Check that the neighbor is in the grid space
    Check that the neighbor is valid (1 = can be visited, 2 = final cell)
    :param grid: map of the maze
    :param neighbor: neighbor[0] = row index | neighbour[1] = col index
    :return: Valid neighbor -> True | Invalid neighbor -> False
    """
    return 0 <= neighbor[0] < len(grid) and \
           0 <= neighbor[1] < len(grid[neighbor[0]]) and \
           (grid[neighbor[0]][neighbor[1]] == 1 or grid[neighbor[0]][neighbor[1]] == 2)


def solve_maze(grid, initial_point, goal_point):
    solution = []
    if solve_maze_rec(grid, initial_point, goal_point, solution):
        print(solution)


def solve_maze_rec(grid, initial_point, goal_point, solution_path):
    grid[initial_point[0], initial_point[1]] = 3  # Mark as visited
    if initial_point == goal_point:
        solution_path.insert(0, goal_point)
        return True
    row = initial_point[0]
    col = initial_point[1]
    if isValid(grid, (row - 1, col)) and solve_maze_rec(grid, (row - 1, col), goal_point, solution_path):
        solution_path.insert(0, (row - 1, col))
        return True
    if isValid(grid, (row + 1, col)) and solve_maze_rec(grid, (row + 1, col), goal_point, solution_path):
        solution_path.insert(0, (row - 1, col))
        return True
    if isValid(grid, (row, col - 1)) and solve_maze_rec(grid, (row, col - 1), goal_point, solution_path):
        solution_path.insert(0, (row - 1, col))
        return True
    if isValid(grid, (row, col + 1)) and solve_maze_rec(grid, (row, col + 1), goal_point, solution_path):
        solution_path.insert(0, (row - 1, col))
        return True
    return False
