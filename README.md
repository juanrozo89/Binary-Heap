# BinaryHeap Class

This BinaryHeap class is an implementation of a binary heap data structure in Python. It supports both max heaps and min heaps and allows you to add elements, remove elements, and perform other common heap operations.

## Features

- Create a max heap or min heap based on your requirement.
- Add elements to the heap while maintaining the heap property.
- Remove elements from the heap while maintaining the heap property.
- Peek at the root element without removing it.
- Get the size of the heap.
- Get the heap as a list.
- Check if the heap contains a specific element.
- Check if the heap is empty.
- Replace the root element while maintaining the heap property.
- Update an element in the heap while maintaining the heap property.
- Clear the heap to remove all elements.
- Build a heap from an unsorted list of elements.

## Usage

```python
from binary_heap import BinaryHeap

# Create a max heap

bh_max = BinaryHeap()

# Create a min heap

bh_min = BinaryHeap(max_heap=False)

# Add elements to the heap

bh_max.add(10)
bh_max.add(8)
bh_max.add(5)
bh_max.add(12)
bh_max.add(7)

# Remove the root element

root = bh_max.poll()

# Check if the heap contains a specific element

if bh_max.contains(8):
print("Heap contains 8")

# Update an element in the heap

bh_max.update(8, 15)

# Print the heap

print(bh_max)
```

## Installation

You can use the BinaryHeap class by simply including the binary_heap.py file in your project.

## Documentation

For more detailed information on the BinaryHeap class and its methods, you can refer to the docstrings provided in the binary_heap.py file.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
