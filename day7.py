from real_inputs.day_7 import real_input

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def part1_helper(l: list, target):
    if len(l) == 2:
        return ({l[0] + l[1]: f"({l[0]}+{l[1]})"} if l[0] + l[1] <= target else {}) | ({l[0] * l[1]: f"({l[0]}*{l[1]})"} if l[0] * l[1] <= target else {})
    else:
        rec = part1_helper(l[:-1], target)
        return {k + l[-1]: f"({v}+{l[-1]})" for k,v in rec.items() if k + l[-1] <= target} | {k * l[-1]: f"({v}*{l[-1]})" for k,v in rec.items() if k * l[-1] <= target}

def part1(text):
    lines = text.split("\n")
    answer = 0
    for line in lines:
        total, values = line.split(": ")
        total = int(total)
        values = [int(v) for v in values.split(" ")]
        possibles = part1_helper(values, total)
        if total in possibles:
            # print(f"{total}: {possibles[total]}")
            answer += total
    return answer

def part2_helper(l: list, target):
    if len(l) == 2:
        return ({l[0] + l[1]} if l[0] + l[1] <= target else set()) | \
            ({l[0] * l[1]} if l[0] * l[1] <= target else set()) | \
            ({int(str(l[0]) + str(l[1]))} if int(str(l[0]) + str(l[1])) <= target else set())
    else:
        rec = part2_helper(l[:-1], target)
        return {k + l[-1] for k in rec if k + l[-1] <= target} | \
            {k * l[-1] for k in rec if k * l[-1] <= target} | \
            {int(str(k) + str(l[-1])) for k in rec if int(str(k) + str(l[-1])) <= target}
    
assert part1(test_input) == 3749
print("\n")
print(part1(real_input))

def part2(text):
    lines = text.split("\n")
    answer = 0
    for line in lines:
        total, values = line.split(": ")
        total = int(total)
        values = [int(v) for v in values.split(" ")]
        possibles = part2_helper(values, total)
        if total in possibles:
            answer += total
    return answer

assert part2(test_input) == 11387
print(part2(real_input))