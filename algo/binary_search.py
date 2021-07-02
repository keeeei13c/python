from typing import List, NewType

IndexNum = NewType('IndexNum', int)


def binary_search(numbers: List[int], value: int) -> IndexNum:
    left, right = 0, len(numbers) - 1
    while left <= right:
        print('###########')
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    nums = [0, 4, 6, 7, 8, 10, 11, 15, 16]
    print(binary_search(nums, 3))
