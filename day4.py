from real_inputs.day_4 import real_input

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def day4part1(text: str):
    rows = [[character for character in row] for row in text.split("\n")]
    width, length = len(rows[0]), len(rows)
    result = 0
    for i in range(length):
        for j in range(width):
            starting_result = result
            if rows[i][j] == 'X' or rows[i][j] == 'S':
                target = ['X', 'M', 'A', 'S'] if rows[i][j] == 'X' else ['S', 'A', 'M', 'X']
                if (i < (width - 3)) and [rows[i+offset][j] for offset in range(4)] == target:
                    result += 1
                if (j < (length - 3)) and [rows[i][j+offset] for offset in range(4)] == target:
                    result += 1
                if (i < (width - 3)) and (j < (length - 3)) and [rows[i+offset][j+offset] for offset in range(4)] == target:
                    result += 1
                if (i < (width - 3)) and (j >= 3) and [rows[i+offset][j-offset] for offset in range(4)] == target:
                    result += 1
            rows[i][j] = '.' if result == starting_result else '!'
    return result

assert day4part1(test_input) == 18
print(day4part1(real_input))

def day4part2(text: str):
    rows = [[character for character in row] for row in text.split("\n")]
    width, length = len(rows[0]), len(rows)
    result = 0
    for i in range(1, length-1):
        for j in range(1, width-1):
            if rows[i][j] == 'A':
                if (rows[i-1][j-1] == 'M' and rows[i+1][j+1] == 'S' \
                or rows[i-1][j-1] == 'S' and rows[i+1][j+1] == 'M') \
                and (rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S' \
                or rows[i-1][j+1] == 'S' and rows[i+1][j-1] == 'M'):
                    result += 1
    return result

assert day4part2(test_input) == 9
print(day4part2(real_input))