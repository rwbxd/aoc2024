from real_inputs.day_5 import real_input
import itertools

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def part1(text):
    dep_dict = {}
    rules, pages = text.split("\n\n")
    for rule in rules.split("\n"):
        l,r = rule.split("|")
        dep_dict.setdefault(r, set()).add(l)

    result = 0
    for line in pages.split("\n"):
        p = line.split(",")
        valid = True
        for i in range(len(p)):
            if p[i] not in dep_dict:
                continue
            for j in range(i+1, len(p)):
                if p[j] in dep_dict[p[i]]:
                    valid = False
                    break
            if not valid: break
        if valid:
            result += int(p[len(p) // 2])
    return result

assert part1(test_input) == 143
print("Part 1:", part1(real_input))

def part2_helper(page_list, dep_dict):
    invalid_tuple = ()
    for i in range(len(page_list)):
        if page_list[i] not in dep_dict: continue
        for j in range(i+1, len(page_list)):
            if page_list[j] in dep_dict[page_list[i]]:
                invalid_tuple = (i,j)
                break
        if len(invalid_tuple): break
    return invalid_tuple

def part2(text):
    dep_dict = {}
    rules, pages = text.split("\n\n")
    for rule in rules.split("\n"):
        l,r = rule.split("|")
        dep_dict.setdefault(r, set()).add(l)
    result = 0
    for line in pages.split("\n"):
        p = line.split(",")
        invalid_tuple = part2_helper(p, dep_dict)
        if not len(invalid_tuple): continue
        while len(invalid_tuple):
            x, y = invalid_tuple
            p[x], p[y] = p[y], p[x]
            invalid_tuple = part2_helper(p, dep_dict)
        result += int(p[len(p)//2])
    return result

assert part2(test_input) == 123
print("Part 2:", part2(real_input))