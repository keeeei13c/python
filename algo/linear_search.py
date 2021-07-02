from typing import List

s = int(input())
def Linear_search(numbers: List[int],value:int) -> int:
    for i in range(0,len(numbers)):
        if numbers[i] == value:
            print(i)
            return i
    return -1


if __name__ == '__main__':
    nums = [0, 4, 6, 7, 8, 10, 11, 15, 16]
    print(Linear_search(nums, s))
