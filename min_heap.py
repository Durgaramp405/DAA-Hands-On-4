from typing import List, TypeVar, Generic
import sys

T = TypeVar('T') 

class MinHeap(Generic[T]):
    def __init__(self, elements: List[T] = None):
        self.heap = elements[:] if elements else []
        if self.heap:
            self.build_min_heap()

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def leftchild(self, index: int) -> int:
        return 2 * index + 1

    def rightchild(self, index: int) -> int:
        return 2 * index + 2

    def heapifydown(self, index: int):
        while True:
            smallest = index
            left = self.leftchild(index)
            right = self.rightchild(index)

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def heapifyup(self, index: int):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            parent_idx = self.parent(index)
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx

    def buildmin_heap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self.heapify_down(i)

    def insert(self, value: T):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
        print(f"Inserted element: {value}")
    
    def pop(self) -> T:
        if not self.heap:
            print("Heap is empty!")
            return None
        root = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self.heapify_down(0)
        print(f"Popped element: {root}")
        return root

    def peek(self) -> T:
        if not self.heap:
            print("Heap is empty!")
            return None
        print(f"Peeked element: {self.heap[0]}")
        return self.heap[0]
    
    def __repr__(self):
        return f"MinHeap({self.heap})"

def main():
    heap = MinHeap()
    while True:
        print("\nChoose an option:")
        print("1. Insert an element")
        print("2. Pop the minimum element")
        print("3. Peek at the minimum element")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                value = int(input("Enter the element to insert: "))
                heap.insert(value)
                print("Heap after insertion:", heap)
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        
        elif choice == "2":
            heap.pop()
            print("Heap after removal:", heap)

        elif choice == "3":
            heap.peek()

        elif choice == "4":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
