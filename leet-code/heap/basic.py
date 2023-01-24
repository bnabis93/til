import sys


class MinHeap:
    """
    Min heap implementation from scartch.
    """
    def __init__(self, maxsize : int = 20) -> None:
        """
        Initialize the heap.
        maxsize is 20 by default.
        """
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = -1 * sys.maxsize
        self.front = 1

    def paraent(self, pos):
        """
        Return the parent position of the given position.
        [root, left_1, right_2, left_1_1, right_1_2, left_2_1, right_2_2]
        """
        return pos // 2

    def left_child(self, pos):
        """
        Return the left child position of the given position.
        """
        return 2 * pos

    def right_child(self, pos):
        """
        Return the right child position of the given position.
        """
        return (2 * pos) + 1

    def is_leaf(self, pos):
        """
        Check if the given position is a leaf node.
        """
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        """
        Swap the values of the given positions.
        fpos is the first position.
        spos is the second position.
        """
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def min_heapify(self, pos):
        """
        Min heapify the heap.
        When I remove the root node, I need to heapify the heap.
        remote the root node mean, get the min value.

        Heapify를 한다는것은 부모노드가 자식노드보다 큰지 확인하고, 크다면 자식노드와 swap을 한다는것이다. (min heap)
        """
        # If the node is a non-leaf node and greater than any of its child -> swap to parent.
        if not self.is_leaf(pos):
            # Swap parent and child if parent is greater than child
            if (self.heap[pos] > self.heap[self.left_child(pos)] or
                self.heap[pos] > self.heap[self.right_child(pos)]):
                # Swap with the left child and heapify the left child
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))
    
    def insert(self, element):
        """
        Insert the element into the heap.
        """
        if self.size >= self.maxsize:
            return "Heap is full"

        self.size += 1
        self.heap[self.size] = element

        current = self.size

        # 최소한의 heapify를 진행한다. 
        while self.heap[current] < self.heap[self.paraent(current)]:
            self.swap(current, self.paraent(current))
            current = self.paraent(current)

    def print_heap(self):
        """
        Print the heap.
        """
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) + " LEFT CHILD : " +
                  str(self.heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.heap[2 * i + 1]))

    def min_heap(self):
        """
        Build the min heap.
        """
        for pos in range(self.size // 2, 0, -1):
            self.min_heapify(pos)

    def remove(self):
        """
        Remove the root node.
        """
        popped = self.heap[self.front]
        # leaf node를 root node로 옮긴다.
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        # left node를 root로 올렸으니 heapify를 한다.
        self.min_heapify(self.front)
        return popped



heap = MinHeap(maxsize=15)
print("system maxsize : ",sys.maxsize)

heap.insert(5)
heap.insert(3)
heap.insert(17)
heap.insert(10)
heap.insert(84)
heap.insert(19)
heap.insert(6)
heap.insert(22)
heap.insert(9)

print(heap.print_heap())
heap.min_heap()
print(heap.print_heap())
print("min value : ", heap.remove())
print(heap.print_heap())
