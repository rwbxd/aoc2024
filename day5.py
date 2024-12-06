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

class Node:
    def __init__(self, val):
        self.val = val
        self.depends_on = set()
    def depend(self, val, seen=None, path=None):
        if not seen: seen = set()
        if self.val in seen: return False
        else: seen.add(self.val)

        if not path: path = []
        if self.val == val: return path + [self.val]

        return any(dep.val == val for dep in self.depends_on)

def part1(text):
    node_dict = {}
    rules, pages = text.split("\n\n")
    for rule in rules.split("\n"):
        l,r = rule.split("|")
        l_node = node_dict.setdefault(l, Node(l))
        r_node = node_dict.setdefault(r, Node(r))
        r_node.depends_on.add(l_node)

    total_valid, total_invalid = 0,0
    result = 0
    for line in pages.split("\n"):
        p = line.split(",")
        valid = True
        for i in range(len(p)):
            if not valid: break
            if p[i] not in node_dict:
                continue
            for j in range(i+1, len(p)):
                if node_dict[p[i]].depend(p[j]):
                    valid = False
                    break
            if not valid: break
        if valid:
            total_valid += 1
            result += int(p[len(p) // 2])
        else: total_invalid += 1
    print(total_valid, total_invalid)
    return result

assert part1(test_input) == 143
print("Part 1:", part1(real_input))

def part2(text):
    node_dict = {}
    rules, pages = text.split("\n\n")
    for rule in rules.split("\n"):
        l,r = rule.split("|")
        l_node = node_dict.setdefault(l, Node(l))
        r_node = node_dict.setdefault(r, Node(r))
        r_node.depends_on.add(l_node)

    result = 0
    for line in pages.split("\n"):
        p = line.split(",")
        valid = True
        highest_valid = 0
        for i in range(len(p)):
            if not valid: break
            if p[i] not in node_dict:
                continue
            for j in range(i+1, len(p)):
                if node_dict[p[i]].depend(p[j]):
                    valid = False
                    break
            if valid: highest_valid = i + 1
        if valid: continue
        else:
            perms = list(itertools.permutations(p[highest_valid:]))
            perm_index = -1
            for perm in perms:
                perm_index += 1
                print(str(perm_index) + "/" + str(len(perms)))
                perm = p[:highest_valid] + list(perm)
                valid = True
                for i in range(len(p)):
                    if not valid: break
                    if perm[i] not in node_dict:
                        continue
                    for j in range(i+1, len(perm)):
                        if node_dict[perm[i]].depend(perm[j]):
                            valid = False
                            break
                if valid:
                    result += int(perm[len(perm)//2])
                    break


    return result

assert part2(test_input) == 123
print("Part 2:", part2(real_input))