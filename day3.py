import re
from real_inputs.day_3 import real_input

test_input ="""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

def day3part1(text):
    matches = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", text)
    return sum(int(match[0]) * int(match[1]) for match in matches)

assert day3part1(test_input) == 161
print(day3part1(real_input))

p2_test_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def day3part2(text):
    groups = text.split("don't()")
    matches = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", groups[0])
    for group in groups[1:]:
        if "do()" not in group: continue
        group = group[group.index("do()"):]
        matches += re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", group)
    return sum(int(match[0]) * int(match[1]) for match in matches)

print(day3part2(p2_test_input))
assert day3part2(p2_test_input) == 48
print(day3part2(real_input))