from real_inputs.day_2 import real_input

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def day2_part1(text):
    return_val = 0
    for line in text.split('\n'):
        nums = [int(x) for x in line.split()]
        increasing = nums[0] < nums[1]
        for i in range(len(nums)-1):
            if (increasing and not 1 <= nums[i+1] - nums[i] <= 3) or (not increasing and not 1 <= nums[i] - nums[i+1] <= 3):
                return_val -= 1
                break
        return_val += 1
    return return_val


assert day2_part1(test_input) == 2
print(day2_part1(real_input))

def day2_part2_helper(nums, first_error=True):
    increasing = nums[0] < nums[1]
    for i in range(len(nums)-1):
        if (increasing and not 1 <= nums[i+1] - nums[i] <= 3) or (not increasing and not 1 <= nums[i] - nums[i+1] <= 3):
            return False
    return True

def day2_part2(text):
    all_nums_lists = [[int(num) for num in line.split()] for line in text.split("\n")]
    acc = 0
    for nums_list in all_nums_lists:
        for i in range(len(nums_list)):
            if day2_part2_helper(nums_list[:i] + nums_list[i+1:]):
                acc += 1
                break
    return acc

assert day2_part2(test_input) == 4
print("Real data")
print(day2_part2(real_input))