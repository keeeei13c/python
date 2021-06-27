from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers

if __name__ == '__main__':
    nums = [83,58,12,63,32,42,43,18,60,93,23,48,14,63,58,43,6,62,29,20,48,64,7,13,48,28,12,42,88,16,24,12,38,28,50,4,6,66,14,69,92,15,90,44,50,64,66,3,68,9,14,66,68,82,59,52,75,30,82,92,25,87,3,71,49,59,96,80,44,39,67,59,73,54,12,38,15,66,8,16,6,46,9,77,83,27,32,45,34,15,96,60,2,39,44,24,12,100,91,8]
    print(bubble_sort(nums))