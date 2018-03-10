import random
import time

def insertion(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i>=0 and (value < list[i]):
            list[i+1] = list[i]
            list[i] = value
            i = i - 1

    return list

a = []
for x in range(15000):
    a.append(random.randint(1, 1001))
a.sort(reverse=True)
print(len(a))
start = time.time()
insertion(a)
elapsed = (time.time() - start)
print(elapsed)
