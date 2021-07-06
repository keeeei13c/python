from typing import List
from random import randint
s = int(input())
def Linear_search(numbers: List[int],value:int) -> int:
    for i in range(0,len(numbers)):
        if numbers[i] == value:
            print(i)
            return i
    return -1


if __name__ == '__main__':
    nums = [randint(1,10000) for _ in range(1,1000)]
    print(Linear_search(nums, s))
