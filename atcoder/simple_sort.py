import time

start = time.time()
process_time = time.time() - start

my_list = []
for i in range(100000000):
    my_list.append(i)

def simple_search(list, item):
    for i in list:
        num = i
        if i == item:
            return num

print(simple_search(my_list, 1))
print(process_time)




