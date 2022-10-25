def is_legit_track(grid, i1, j1, i2, j2, current_weight):
    if i2 < 0 or j2 < 0 or i2 >= len(grid) or j2 >= len(grid[0]):
        return False
    if (i1 == i2 + 1 and j1 == j2) or (i1 == i2 - 1 and j1 == j2) or \
            (i1 == i2 and j1 == j2 + 1) or (i1 == i2 and j1 == j2 - 1):
        if current_weight + grid[i2][j2] < 2 * grid[i2][j2]:
            return True
    return False


def get_number_legit_tracks(grid, i1, j1):
    def get_number_legit_tracks_helper(grid, i1, j1, current_weight):
        if len(grid) - 1 == i1 and len(grid[0]) - 1 == j1:
            return 1
        num_of_paths = 0
        if is_legit_track(grid, i1, j1, i1 + 1, j1, current_weight + grid[i1][j1]):
            num_of_paths += get_number_legit_tracks_helper(grid, i1 + 1, j1, grid[i1][j1] + current_weight)

        if is_legit_track(grid, i1, j1, i1, j1 + 1, current_weight + grid[i1][j1]):
            num_of_paths += get_number_legit_tracks_helper(grid, i1, j1 + 1, grid[i1][j1] + current_weight)

        if is_legit_track(grid, i1, j1, i1 - 1, j1, current_weight + grid[i1][j1]):
            num_of_paths += get_number_legit_tracks_helper(grid, i1 - 1, j1, grid[i1][j1] + current_weight)

        if is_legit_track(grid, i1, j1, i1, j1 - 1, current_weight + grid[i1][j1]):
            num_of_paths += get_number_legit_tracks_helper(grid, i1, j1 - 1, grid[i1][j1] + current_weight)

        return num_of_paths

    return get_number_legit_tracks_helper(grid, i1, j1, 0)


grid = [
    [0, 1, 2],
    [1, 2, 4],
    [2, 4, 8]
]
print(is_legit_track(grid, 0, 0, 1, 0, 0))
print(is_legit_track(grid, 0, 0, 1, 1, 0))
print(is_legit_track(grid, 2, 0, 2, 1, 3))
print(get_number_legit_tracks(grid, 0, 0))
