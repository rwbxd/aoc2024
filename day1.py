from real_inputs.day_1 import real_input

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

def day1part1(text):
    l_arr, r_arr = [], []
    for l, r in [t.split() for t in text.split("\n")]:
        l_arr.append(int(l))
        r_arr.append(int(r))
    sum = 0
    for l, r in zip(sorted(l_arr), sorted(r_arr)):
        sum += l - r if l > r else r - l
    print(sum)
    return sum

assert day1part1(test_input) == 11
print(day1part1(real_input))

def day1part2(text):
    l_dict, r_dict = {}, {}
    for l, r in [t.split() for t in text.split("\n")]:
        l_dict[l] = l_dict.get(l, 0) + 1
        r_dict[r] = r_dict.get(r, 0) + 1
    return_val = sum(int(l) * l_dict[l] * r_dict.get(l, 0) for l in l_dict.keys())
    print(return_val)
    return return_val

assert day1part2(test_input) == 31
print(day1part2(real_input))