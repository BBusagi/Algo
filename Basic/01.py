#01 Design Dynamic Array (Resizable Array)  `[Easy] `
''''''
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        if i >= self.size:
            raise ValueError("Out of size")
        return self.arr[i]

    def insert(self, i: int, n: int) -> None:
        if i >= self.size:
            raise ValueError("Out of size")
        if self.arr[i] is not None:
            self.size -=1
        self.arr[i] = n
        self.size += 1

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise ValueError("Array is empty")
    
        #soft deletion
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
