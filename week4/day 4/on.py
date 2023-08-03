# def binary_search(array, value_to_search):
#     middle = array[len(array) // 2]
#     right = len(array)
#     left = 0
#     iteration = 0

#     while left == middle or right == middle:
#         iteration += 1

#         if middle == value_to_search:
#             print(f"FOUND SEARCH VALUE - {value_to_search}!")
#             print(f"Iterations", iteration)
#             break

#         elif middle < value_to_search:
#             left = middle
#             middle = (left + right) // 2

#         elif middle > value_to_search:
#             right = middle
#             middle = (left + right) // 2
#         print(left, "left")
#         print(right, "right")
#     else:
#         print("NO SUCH VALUE")


# some_array = list(range(1000))
# value = 1500

# binary_search(some_array, value)

array = [2, 4, 6, 8, 10]


def sum_array(array):
    if len(array) == 1:
        return array[0]
    else:
        middle = len(array) // 2
        left_sum = sum_array(array[:middle])
        right_sum = sum_array(array[middle:])

        return left_sum + right_sum


print(sum_array(array))
