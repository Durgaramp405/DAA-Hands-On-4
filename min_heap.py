from typing import List, TypeVar, Generic

T = TypeVar('T')

class MinHeap(Generic[T]):
    def __init__(self, elements: List[T] = None):
        self.heap = elements if elements else []
        if self.heap:
            self.build_min_heap()
    
    def parent(self, i: int) -> int:
        return (i - 1) >> 1  
    
    def left_child(self, i: int) -> int:
        return (i << 1) + 1  
    
    def right_child(self, i: int) -> int:
        return (i << 1) + 2 
    
    
    def heapify(self, i: int):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)
    
    def build_min_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)
    
    def push(self, item: T):
        self.heap.append(item)
        index = len(self.heap) - 1
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def pop(self) -> T:
        if not self.heap:
            raise IndexError("Pop from empty heap")
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.heapify(0)
        return root
    
    def peek(self) -> T:
        if not self.heap:
            raise IndexError("Peek from empty heap")
        return self.heap[0]
    
    def __repr__(self):
        return str(self.heap)

# Example Usage
def test_min_heap():
    print("Building heap from [5, 3, 4, 1, 2, 6]")
    heap = MinHeap([5, 3, 4, 1, 2, 6])
    print("Heap after build_min_heap:", heap)
    
    print("Pushing 0 into heap")
    heap.push(0)
    print("Heap after push:", heap)
    
    print("Popping root element:", heap.pop())
    print("Heap after pop:", heap)
    
    print("Peeking root element:", heap.peek())
    print("Final heap state:", heap)

if __name__ == "__main__":
    test_min_heap()