from real_inputs.day_8 import real_input

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def part1(text):
    antennas = {}
    grid = [list(row) for row in text.split("\n")]
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val != '.': antennas.setdefault(val, set()).add((j,i))
    antinodes = set()
    x_min, x_max = 0, len(grid[0]) - 1
    y_min, y_max = 0, len(grid) - 1
    for freq in antennas:
        if len(antennas[freq]) == 1: continue
        for first in antennas[freq]:
            for second in antennas[freq]:
                if first == second: continue
                x_change = second[0] - first[0]
                y_change = second[1] - first[1]
                if x_min <= (second[0] + x_change) <= x_max and \
                    y_min <= (second[1] + y_change) <= y_max:
                    antinodes.add((second[0] + x_change, (second[1] + y_change)))
    return len(antinodes)

assert part1(test_input) == 14
print(part1(real_input))

def part2(text):
    antennas = {}
    grid = [list(row) for row in text.split("\n")]
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val != '.': antennas.setdefault(val, set()).add((j,i))
    antinodes = set()
    x_min, x_max = 0, len(grid[0]) - 1
    y_min, y_max = 0, len(grid) - 1
    for freq in antennas:
        if len(antennas[freq]) == 1: continue
        for first in antennas[freq]:
            for second in antennas[freq]:
                if first == second: continue
                x_change = second[0] - first[0]
                y_change = second[1] - first[1]
                while x_min <= (second[0] + x_change) <= x_max and \
                    y_min <= (second[1] + y_change) <= y_max:
                    antinodes.add((second[0] + x_change, (second[1] + y_change)))
                    x_change += second[0] - first[0]
                    y_change += second[1] - first[1]

    return len(antinodes) + sum((sum(1 if x not in antinodes else 0 for x in v) for v in antennas.values()))

assert part2(test_input) == 34
print(part2(real_input))