import numpy as np

class SortArray:
    def __init__(self, arr):
        self.arr = arr
        
    def bubble_sort(self):
        n = len(self.arr)
        
        for i in range(n):
            for j in range(n-i-1):
                
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    
        return self.arr

random_arr = np.random.randint(1, 101, size=7)
print(random_arr)

# sa = SortArray(random_arr)
# bubble_sort_arr = sa.bubble_sort()

# print(bubble_sort_arr)

random_arr = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(random_arr)
print("length of an array", n)

for i in range(1, n):
    insert_index = i
    current_value = random_arr[i]
    print("\nIteration", i)
    print("Insert index:", insert_index)
    print("Current value:", current_value)

    for j in range(i - 1, -1, -1):
        if random_arr[j] > current_value:
            random_arr[j + 1] = random_arr[j]
            insert_index = j
        else:
            break
    random_arr[insert_index] = current_value
    print("Array after insertion:", random_arr)

print("\nSorted array:", random_arr)
