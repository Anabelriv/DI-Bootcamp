# Given a list of numbers and a target, write a function to determine if the target can be calculated by summing together any 2 numbers in the list.
# The function should return True if the target can be calculated and False if not.

# For ease of analysis and to see whats going on, we will also print True and the 2 numbers, or False.
# def subsetsum(numbers: list, target: int) -> bool:
#     # <your code here>
# Notes:

# The list is of arbitrary length.
# The list is unsorted.
# The list may contain both positive and negative integers.
# There may be duplicated numbers.
# Example Outputs
# nums = [12, -7, 20, 1, 4, -10, -1]

# subsetsum(nums, 1) # False
# subsetsum(nums, 2) # True: 12,  -10
# subsetsum(nums, 3) # True: 4,  -1
# subsetsum(nums, 4) # False
# Big O Considerations
# What is the Big O complexity of your solution?
# Can you improve it?
# What if the numbers list is 100K or 10M items long? Is your solution still feasible?


# def subsetsum(numbers: list, target: int) -> bool:
#     seen = set()
#     for num in numbers:
#         if target - num in seen:
#             print("True:", target - num, num)
#             return True
#         seen.add(num)
#     print("False")
#     return False


# # Test
# nums = [12, -7, 20, 1, 4, -10, -1]
# subsetsum(nums, 1)  # False
# subsetsum(nums, 2)  # True: -10, 12
# subsetsum(nums, 3)  # True: -1, 4
# subsetsum(nums, 4)  # False

# The Big O complexity of this solution is O(N), where N is the number of elements in the list. The reason for this is that for each element in the list, we perform a constant time operation of checking if the difference between the target and the current element is in the set. The set has an average constant time complexity for add and lookup operations.

# This solution is efficient and feasible even for large lists of 100K or 10M items. The time complexity remains linear, and the execution time would depend on the size of the list. In practice, it should be able to handle such large lists without any issues.


# Problem 2

# To find the length of the longest consecutive number sequence in the given unsorted list of integers, we can use a HashSet (Python's set data structure). The idea is to first add all the numbers to the set for quick lookups. Then, for each number in the list, we check if its previous number (number - 1) is present in the set. If not, it means this number is the start of a sequence. We then keep counting the consecutive numbers in the sequence until we reach the end of the sequence. While counting, we can remove the numbers from the set to avoid redundant checks.


# def longest_sequence(nums: list) -> int:
#     num_set = set(nums)
#     max_length = 0

#     for num in nums:
#         if num - 1 not in num_set:  # This is the start of a sequence
#             current_num = num
#             while current_num in num_set:
#                 current_num += 1
#             max_length = max(max_length, current_num - num)

#     return max_length

# # Test
# nums = [6, 4, 100, 5, 200, 2, 3]
# print(longest_sequence(nums))  # Output: 5

# The Big O complexity of this solution is O(N), where N is the number of elements in the list. The time complexity is mainly due to the initial setup of the set, which takes O(N) time. The subsequent loop through the list also takes O(N) time as each element is visited at most twice (once for checking if it is the start of a sequence and once for counting the consecutive numbers).

# This solution is efficient and feasible even for large lists of 100K or 10M items. The time complexity remains linear, and the execution time would depend on the size of the list. In practice, it should be able to handle such large lists without any issues.


# def recursive_sum(nums):
#     if not nums:  # Base case: an empty list has a sum of 0
#         return 0
#     else:
#         return nums[0] + recursive_sum(
#             nums[1:]
#         )  # Recursive call with the rest of the list


# # Test
# nums = [2, 4, 5, 6, 7]
# print(recursive_sum(nums))  # Output: 24


# def recursive_reverse_string(s):
#     if not s:  # Base case: an empty string has no reverse
#         return ""
#     else:
#         return (
#             recursive_reverse_string(s[1:]) + s[0]
#         )  # Recursive call with the rest of the string


# # Test
# string = "Hello World!"
# print(recursive_reverse_string(string))  # Output: "!dlroW olleH"

# 3. **Power of a Number:**

#     Write a recursive function to calculate the power of a number. The function should take base and exponent as input and return the result.

#     Input: `2, 3` (i.e., `2^3`)
#     Output: `8`


def power(base, exponent):
    if exponent == 0:  # Base case: any number raised to the power of 0 is 1
        return 1
    if exponent > 0:
        return base * power(
            base, exponent - 1
        )  # Recursive call with the exponent decreased by 1
    else:
        return 1 / (base * power(base, abs(exponent) - 1))  # for negative


# Base is the same and just exponent changes, we call the function of "power"
# Test
base_num = 2
exponent_num = 1
result = power(base_num, exponent_num)
print(result)  # Output: 8 (2^3 = 8)
