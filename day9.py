from real_inputs.day_9 import real_input
test_input = """2333133121414131402"""

def part1(text):
    file_index = 0
    file_system = []
    file = True
    for x in list(text):
        file_system += [file_index if file else '.'] * int(x)
        if file: file_index += 1
        file = not file
    l_index, r_index = 0, len(file_system) - 1
    checksum = 0
    while l_index < r_index:
        if file_system[l_index] != '.':
            checksum += file_system[l_index] * l_index
        else:
            while file_system[r_index] == '.':
                r_index -= 1
            checksum += file_system[r_index] * l_index
            r_index -= 1
        l_index += 1
    if l_index == r_index:
        if file_system[l_index] != '.':
            checksum += file_system[l_index] * l_index
    return checksum

assert part1(test_input) == 1928
print(part1(real_input))

def part2(text):
    file_index = 0
    file_system = []
    file = True
    for x in list(text):
        file_system += [file_index if file else '.'] * int(x)
        if file: file_index += 1
        file = not file
    # print(file_system)
    r_index = len(file_system) - 1
    moved = set()
    while file_system[r_index] != 0:
        if file_system[r_index] == '.':
            r_index -= 1
            continue
        r_value = file_system[r_index]
        while r_value in moved and r_index >= 0:
            r_index -= 1
            r_value = file_system[r_index]
        moved.add(r_value)
        end_r_index = r_index
        r_count = 0
        while file_system[r_index] == r_value:
            r_count += 1
            r_index -= 1
        l_index = 0
        while l_index < r_index:
            while file_system[l_index] != '.':
                l_index += 1
            if l_index > r_index: break
            # Start check of new segment
            start_l_index = l_index
            l_count = 0
            while file_system[l_index] == '.':
                l_count += 1
                l_index += 1
            if r_count <= l_count:
                while r_count > 0:
                    file_system[start_l_index] = r_value
                    file_system[end_r_index] = '.'
                    end_r_index -= 1
                    start_l_index += 1
                    r_count -= 1
                break
    
    checksum = 0
    for i in range(len(file_system)):
        if file_system[i] == '.': continue
        checksum += i * file_system[i]
    # print(file_system)
    # print(checksum)
    return checksum

assert part2(test_input) == 2858
print(part2(real_input))