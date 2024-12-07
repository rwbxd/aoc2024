from real_inputs.day_6 import real_input
from time import sleep

test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def part1(text, debug=False):
    seen = set()
    grid = [[square for square in line] for line in text.split("\n")]
    dir = [-1, 0]
    guard = [-1, -1]
    for r, row in enumerate(grid):
        if '^' in row:
            guard[0] = r
            guard[1] = row.index('^')
            break
    total = 0
    try:
        while (f"{guard}, {dir}") not in seen and not (guard[0] < 0 or guard[1] < 0):
            old_guard_square, grid[guard[0]][guard[1]] = grid[guard[0]][guard[1]], '^'
            if debug:
                sleep(4)
                print(total)
                print("\n" * 3)
                print("\n".join("".join(row) for row in grid))
            grid[guard[0]][guard[1]] = old_guard_square
            if grid[guard[0]][guard[1]] != 'X':
                grid[guard[0]][guard[1]] = 'X'
                total += 1
            next = (guard[0] + dir[0], guard[1] + dir[1])
            if next[0] < 0 or next[1] < 0:
                break
            while grid[next[0]][next[1]] == '#':
                dir = [dir[1], -1 *  dir[0]]
                next = (guard[0] + dir[0], guard[1] + dir[1])
            guard = next
    except:
        pass
    return total

assert part1(test_input) == 41
assert (expected := part1(".\n.\n.\n^")) == 4, f"{expected} != 4"
assert (expected := part1("#...\n^...")) == 4, f"{expected} != 4"
assert (expected := part1("#...\n^..#")) == 3, f"{expected} != 3"
assert (expected := part1(
    """####
...#
#.##
#^##
#.##""")) == 5, f"{expected} != 5"
print(part1(real_input))

def part2helper(text):
    seen = set()
    grid = [[square for square in line] for line in text.split("\n")]
    dir = [-1, 0]
    guard = [-1, -1]
    for r, row in enumerate(grid):
        if '^' in row:
            guard[0] = r
            guard[1] = row.index('^')
            break
    total = 0
    try:
        while (f"{guard}, {dir}") not in seen and not (guard[0] < 0 or guard[1] < 0):
            seen.add(f"{guard}, {dir}")
            old_guard_square, grid[guard[0]][guard[1]] = grid[guard[0]][guard[1]], '^'
            grid[guard[0]][guard[1]] = old_guard_square
            if grid[guard[0]][guard[1]] != 'X':
                grid[guard[0]][guard[1]] = 'X'
                total += 1
            next = (guard[0] + dir[0], guard[1] + dir[1])
            if next[0] < 0 or next[1] < 0:
                break
            while grid[next[0]][next[1]] == '#':
                dir = [dir[1], -1 *  dir[0]]
                next = (guard[0] + dir[0], guard[1] + dir[1])
            guard = next
    except:
        pass
    return grid

def part2(text, debug=False):
    initial_grid = part2helper(text)
    total = 0
    for i in range(len(initial_grid)):
        for j in range(len(initial_grid[0])):
            if initial_grid[i][j] != 'X': continue
            seen = set()
            grid = [[square for square in line] for line in text.split("\n")]
            grid[i][j] = '#'
            dir = [-1, 0]
            guard = [-1, -1]
            for r, row in enumerate(grid):
                if '^' in row:
                    guard[0] = r
                    guard[1] = row.index('^')
                    break
            try:
                while (f"{guard}, {dir}") not in seen:
                    seen.add(f"{guard}, {dir}")
                    old_guard_square, grid[guard[0]][guard[1]] = grid[guard[0]][guard[1]], '^'
                    if debug:
                        print(total)
                        print("\n" * 3)
                        print("\n".join("".join(row) for row in grid))
                    grid[guard[0]][guard[1]] = old_guard_square
                    if grid[guard[0]][guard[1]] != 'X':
                        grid[guard[0]][guard[1]] = 'X'
                    next = (guard[0] + dir[0], guard[1] + dir[1])
                    if (next[0] < 0 or next[1] < 0): break
                    while grid[next[0]][next[1]] == '#':
                        dir = [dir[1], -1 *  dir[0]]
                        next = (guard[0] + dir[0], guard[1] + dir[1])
                    guard = next
                    if (guard[0] < 0 or guard[1] < 0): break
            except:
                pass
            if f"{next}, {dir}" in seen: total += 1
    print(total)
    return total

assert part2(test_input, True) == 6
print(part2(real_input))