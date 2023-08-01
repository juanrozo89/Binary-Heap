import math
COMPARABLE_TYPES = (int, float, complex, str)

class BinaryHeap():
    def __init__(self, max_heap = True, elem_type = None):
        """
        Initialize a BinaryHeap instance.

        Parameters:
            max_heap (bool, optional): If True, the binary heap will be a max heap,
                otherwise, it will be a min heap. Default is True (max heap).
            elem_type (type, optional): The predefined type for elements to be added to the binary heap.
                If provided, the binary heap will only accept elements of this type. Default is None.

        Attributes:
            heap (list): A list to store the elements of the binary heap.
            max_heap (bool): If True, the binary heap is a max heap, otherwise, it
                is a min heap.
            type (type, None): Stores the data type of the first element(s) 
                added to the heap. When elements are added to the heap, 
                it will be updated to the data type of the first element added
                and will be used to maintain consistency for subsequent additions.

        Example:
            >>> bh_max = BinaryHeap()
            >>> bh_min = BinaryHeap(max_heap=False, elem_type=int)

        Note:
            If the 'elem_type' parameter is provided, the binary heap will only accept elements of the specified type.
            If 'elem_type' is not provided (left as None), the binary heap will initially accept elements of any comparable type.

        Raises:
            TypeError: If the 'elem_type' parameter is provided and it is not a valid type.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if elem_type is not None and elem_type not in COMPARABLE_TYPES:
            raise TypeError(f"Invalid element type. The element must be one of the supported comparable types: int, float, complex, or str. Received: {elem_type}")
        self.heap = []
        self.max_heap = max_heap
        self.type = elem_type


    def __repr__(self):
        """
        Return a string representation of the binary heap.

        The string representation displays the elements in the binary heap in a tree-like
        structure, following the level-order traversal. Each level is separated by a new line.

        Returns:
            str: A string representation of the binary heap.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> bh.add(7)
            >>> print(bh)
            [12]
            [10][7]
            [8][5]

        Time Complexity:
            O(n) where n is the number of elements in the heap

        Space Complexity:
            O(n) where n is the number of elements in the heap
        """

        if self.is_empty():
            return "- Empty heap -"

        to_return = ""
        curr_level = 1
        for i in range(self.size()):
            level = int(1 + math.log(i+1, 2))
            if level == curr_level:
                to_return += f"[{self.heap[i]}]"
            else:
                to_return += f"\n[{self.heap[i]}]"
                curr_level = level
        return to_return


    def _is_valid_type(self, elem):
        """
        Check if the given element has a valid comparable type for the binary heap.

        This method verifies if the data type of the element is one of the supported
        comparable types (int, float, complex, or str) that can be used in the binary heap,
        or if the heap already has an assigned type, it verifies if the type of the element 
        is consistent

        Parameters:
            elem (Any): The element whose type needs to be checked.

        Returns:
            bool: True if the element's type is valid, False otherwise.

        Example:
            >>> bh = BinaryHeap()
            >>> bh._is_valid_type(10)
            True
            >>> bh._is_valid_type("hello")
            True
            >>> bh._is_valid_type([1, 2, 3])
            False

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if (self.type is None and not isinstance(elem, COMPARABLE_TYPES)) \
            or (self.type is not None and self.type != type(elem)):
            return False
        return True


    def size(self):
        """
        Return the number of elements currently in the binary heap.

        Returns:
            int: The number of elements in the binary heap.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.size()  # Output: 3

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.heap)


    def get_heap(self):
        """
        Retrieve the binary heap as a list.

        Returns:
            list: A list containing all elements in the binary heap.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> bh.get_heap()  # Output: [12, 10, 5, 8]

        Notes:
            - The order of elements in the returned list might not represent the exact
            internal structure of the binary heap, as the list is provided without
            performing any additional transformations or heap property checks.

        Time Complexity:
            O(1)

        Space Complexity:
            O(n) where n is the number of elements in the heap
        """
        return self.heap.copy()
    

    def peek(self):
        """
        Return the root element of the binary heap without removing it.

        Returns:
            Union[None, int, float, complex, str]: The root element if the binary heap is not empty, otherwise returns None.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(12)
            >>> bh.add(7)
            >>> print(bh.peek())  # Output: 12

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return self.heap[0]  


    def parent(self, i):
        """
        Return the parent element at the given index 'i' in the binary heap.

        Parameters:
            i (int): The index of the element in the binary heap.

        Returns:
            Union[None, int, float, complex, str]: The parent element if 'i' is a valid index and has a parent,
            or None if 'i' is 0.

            Raises:
                IndexError: If 'i' is out of bounds.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> bh.add(7)
            >>> print(bh.parent(3))  # Output: 10
            >>> print(bh.parent(0))  # Output: None
            >>> print(bh.parent(6))  # Raises IndexError

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if i == 0:
            return None
        elif i < 0 or i >= self.size():
            raise IndexError("Index out of bounds")
        else: 
            index = (i - 1) // 2
            return self.heap[index]


    def left_child(self, i):
        """
        Return the left child element at the given index 'i' in the binary heap.

        Parameters:
            i (int): The index of the element in the binary heap.

        Returns:
            Union[None, int, float, complex, str]: The left child element if 'i' is a valid index and has a left child,
            otherwise returns None if 'i' has no left child.

        Raises:
            IndexError: If 'i' is out of bounds.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> bh.add(7)
            >>> print(bh.left_child(1))  # Output: 5
            >>> print(bh.left_child(4))  # Output: None
            >>> print(bh.left_child(6))  # Raises IndexError

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if i < 0 or i >= self.size():
            raise IndexError("Index out of bounds")
        else: 
            index = (i * 2) + 1
            if index < self.size():
                return self.heap[index]
            return None


    def right_child(self, i):
        """
        Return the right child element at the given index 'i' in the binary heap.

        Parameters:
            i (int): The index of the element in the binary heap.

        Returns:
            Union[None, int, float, complex, str]: The right child element if 'i' is a valid index and has a right child,
            otherwise returns None if 'i' has no right child.

        Raises:
            IndexError: If 'i' is out of bounds.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> bh.add(7)
            >>> print(bh.right_child(1))  # Output: 7
            >>> print(bh.right_child(4))  # Output: None
            >>> print(bh.right_child(6))  # Raises IndexError
        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if i < 0 or i >= self.size():
            raise IndexError("Index out of bounds")
        else: 
            index = (i * 2) + 2
            if index < self.size():
                return self.heap[index]
            return None
    

    def children(self, i):
        """
        Return both left and right child of the element at the given index 'i' in the binary heap.

        Parameters:
            i (int): The index of the element in the binary heap.

        Returns:
            Tuple[Union[None, int, float, complex, str], Union[None, int, float, complex, str]]: A tuple containing the left and right child elements.
                If the left child does not exist, it will be None.
                If the right child does not exist, it will be None. 

        Raises:
            IndexError: If 'i' is out of bounds.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> bh.add(7)
            >>> left_child, right_child = bh.children(1)
            >>> print(left_child, right_child)  # Output: 5 7

            >>> left_child, right_child = bh.children(4)
            >>> print(left_child, right_child)  # Output: None None

            >>> left_child, right_child = bh.children(5)  # Raises IndexError

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if i < 0 or i >= self.size():
            raise IndexError("Index out of bounds")
        return (self.left_child(i), self.right_child(i))


    def _check_child_invariance(self, i):
        """
        Check the invariance property for a given element at index 'i' in the binary heap.

        Parameters:
            i (int): The index of the element in the binary heap.

        Returns:
            bool: True if the invariance property holds for the element at index 'i', otherwise False.

        Raises:
            IndexError: If 'i' is out of bounds.

        Time Complexity:
            O(1)
        
        Space Complexity:
            O(1)
        """
        if i >= self.size():
            raise IndexError("Index out of bounds")
        elif self.max_heap:
            if (self.left_child(i) is not None and self.heap[i] < self.left_child(i)) \
                or (self.right_child(i) is not None and self.heap[i] < self.right_child(i)):
                return False
        elif (self.left_child(i) is not None and self.heap[i] > self.left_child(i)) \
                or (self.right_child(i) is not None and self.heap[i] > self.right_child(i)):
                return False
        return True


    def _heapify_up(self, i):
        """
        Move the element at the given index 'i' upwards in the binary heap to maintain the heap property.

        This method is used after adding an element to the binary heap to ensure that the heap property is preserved.

        Parameters:
            i (int): The index of the element to be moved upwards.

        Raises:
            IndexError: If 'i' is out of bounds.

        Time Complexity:
            O(log n) where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if i < 0 or i >= self.size():
            raise IndexError("Index out of bounds")
        
        parent_i = (i - 1) // 2
        while parent_i >= 0 and not self._check_child_invariance(parent_i):
            temp = self.heap[parent_i]
            self.heap[parent_i] = self.heap[i]
            self.heap[i] = temp
            i = parent_i
            parent_i = (i - 1) // 2


    def _heapify_down(self, i):
        """
        Move the element at the given index 'i' downwards in the binary heap to maintain the heap property.

        This method is used after removing an element from the binary heap to ensure that the heap property is preserved.

        Parameters:
            i (int): The index of the element to be moved downwards.

        Raises:
            IndexError: If 'i' is out of bounds.

        Time Complexity:
            O(log n) where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if i < 0 or i >= self.size():
            raise IndexError("Index out of bounds")
        
        while not self._check_child_invariance(i):
            left_i = (i * 2) + 1
            right_i = (i * 2) + 2
            if (self.max_heap and self.heap[left_i] >= self.heap[right_i]) or \
            (not self.max_heap and self.heap[left_i] <= self.heap[right_i]):
                temp = self.heap[left_i]
                self.heap[left_i] = self.heap[i]
                self.heap[i] = temp
                i = left_i
            else:
                temp = self.heap[right_i]
                self.heap[right_i] = self.heap[i]
                self.heap[i] = temp
                i = right_i


    def is_empty(self):
        """
        Check if the binary heap is empty.

        Returns:
            bool: True if the binary heap is empty, otherwise False.

        Example:
            >>> bh = BinaryHeap()
            >>> print(bh.is_empty())  # Output: True
            >>> bh.add(10)
            >>> print(bh.is_empty())  # Output: False

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return self.size() == 0;


    def contains(self, elem):
        """
        Check if the binary heap contains a specific element.

        Parameters:
            element (int or float or complex or str): The element to check for in the binary heap.

        Returns:
            bool: True if the element is found in the binary heap, otherwise False.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> print(bh.contains(8))  # Output: True
            >>> print(bh.contains(12))  # Output: False

        Time Complexity:
            O(n) where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        return elem in self.heap
    

    def add(self, elem):
        """
        Add a new element to the binary heap while maintaining the heap property.

        Parameters:
            elem: The element to be added to the binary heap. The element must be of one
                of the following types: int, float, complex, or str. If the binary heap
                already contains elements, the new element's type must be consistent with
                the type of the first element(s) added to the heap.

        Raises:
            TypeError: If the element's type is not one of the supported comparable types
                    (int, float, complex, or str), or if the element's type is inconsistent
                    with the types of the existing elements in the binary heap.

        Example:
            >>> bh_num = BinaryHeap()
            >>> bh_num.add(10)
            >>> bh_num.add(8)
            >>> bh_num.add(5)
            >>> bh_str = BinaryHeap()
            >>> bh_str.add("apple")
            >>> bh_str.add("orange")
            >>> bh_str.add(5)    # Raises TypeError

        Notes:
            - If the binary heap has no assigned datatype, the type of the first added element is used as
            a reference type to ensure consistency for subsequent additions.

        Time Complexity:
            O(log n) where n is the number of elements in the heap

        Space Complexity:
            O(1)
        """

        if not self._is_valid_type(elem):
            if self.type is not None:
                raise TypeError(f"Invalid element type. The element must be of type {self.type}. Received: {type(elem)}")
            else: 
                raise TypeError(f"Invalid element type. The element must be one of the supported comparable types: int, float, complex, or str. Received: {type(elem)}")     
        elif self.type is None:
            self.type = type(elem)

        self.heap.append(elem)
        if self.size() > 1:
            i = self.size() - 1
            self._heapify_up(i)


    def remove(self, elem):
        """
        Remove a specific element from the binary heap if it exists.

        Parameters:
            element (int or float or complex or str): The element to be removed from the binary heap.

        Returns:
            Union[None, int, float, complex, str]: The removed element if it was found in the binary heap, 
            otherwise returns None if the element was not present in the heap.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> print(bh.remove(8))  # Output: 8
            >>> print(bh.remove(12))  # Output: None

        Time Complexity:
            O(log n) where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if not self.contains(elem):
            return None

        i = self.heap.index(elem)
        self.heap[i] = self.heap.pop()
        self._heapify_down(i)
        return elem


    def poll(self):
        """
        Remove and return the root element of the binary heap while maintaining the heap property.

        Returns:
            int or None: The root element if the binary heap is not empty, otherwise returns None.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(12)
            >>> bh.add(7)
            >>> print(bh.poll())  # Output: 12

        Time Complexity:
            O(log n) where n is the number of elements in the heap

        Space Complexity:
            O(1)
        """
        if self.size() == 0:
            return None
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._heapify_down(0)
        return root
    

    def replace(self, new_root):
        """
        Replace the root element of the binary heap with a new element while maintaining the heap property.

        Parameters:
            new_elem (int or float or complex or str): The new element to replace the root.

        Returns:
            Union[None, int, float, complex, str]: The original root element that was replaced, 
            or None if the heap is empty.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> print(bh.replace(15))  # Output: 12

        Time Complexity:
            O(log n) where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if self.is_empty():
            return None
        
        to_return = self.heap[0]
        self.heap[0] = new_root
        self._heapify_down(0)
        return to_return
    

    def update(self, old_elem, new_elem):
        """
        Update a specific element in the binary heap with a new element while maintaining the heap property.

        Parameters:
            old_elem (int or float or complex or str): The element to be updated in the binary heap.
            new_elem (int or float or complex or str): The new element to replace the old element.

        Returns:
            bool: True if the update was successful (old_elem was found and replaced), False otherwise.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.add(12)
            >>> bh.update(8, 15)
            >>> print(bh)  
            [15]
            [12][5]
            [10]

        Notes:
            - The method will perform the necessary heapify operations to maintain the heap property.
            - If the old element is not present in the binary heap, the method will not make any changes and return False.

        Time Complexity:
            O(n) where n is the number of elements in the heap.

        Space Complexity:
            O(1)
        """
        if not self.contains(old_elem):
            return False
        
        i = self.heap.index(old_elem)
        self.heap[i] = new_elem
        if (new_elem > old_elem and self.max_heap) \
            or (new_elem < old_elem and not self.max_heap):
            self._heapify_up(i)
        else: 
            self._heapify_down(i)
        return True
    

    def clear(self):
        """
        Clear all elements from the binary heap.

        After calling this method, the binary heap will be empty, and all its elements will be removed.

        Example:
            >>> bh = BinaryHeap()
            >>> bh.add(10)
            >>> bh.add(8)
            >>> bh.add(5)
            >>> bh.clear()
            >>> print(bh.is_empty())  # Output: True

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.heap = []


    def build_heap(self, elements):
        """
        Build a binary heap from an unsorted list of elements.

        This method transforms the internal list representation of the binary heap
        into a valid binary heap that satisfies the heap property. The elements
        passed as the argument should be in an unsorted order.

        Parameters:
            elements (list): The list of elements to be transformed into a binary heap.

        Raises:
            TypeError: If the 'elements' parameter is not a list.
            TypeError: If an element in the list has not a valid type.

        Example:
            >>> bh = BinaryHeap()
            >>> elements = [7, 12, 3, 8, 5]
            >>> bh.build_heap(elements)
            >>> print(bh)
            [12]
            [8][3]
            [7][5]
    
        Note:
            The method does not clear the existing elements in the binary heap. If the
            heap is not empty when 'build_heap' is called, the new elements will be added
            to the existing heap, and the heap property will be restored.

        Time Complexity:
            O(n) where n is the number of elements in the input list

        Space Complexity:
            O(n) where n is the number of elements in the input list
        """
        if not isinstance(elements, list):
            raise TypeError(f"Expected a list as the argument, but received {type(elements)} instead.")
        
        potential_type = None

        for elem in elements:
            if not self._is_valid_type(elem):
                if self.type is not None:
                    raise TypeError(f"Invalid element type. The element must be of type {self.type}. Received: {type(elem)}")
                else:
                    raise TypeError(f"Invalid element type. The element must be one of the supported comparable types: int, float, complex, or str. Received: {type(elem)}")
            elif potential_type is not None and type(elem) != potential_type:
                raise TypeError(f"All elements in the list must have the same type. Expected {potential_type}. Received: {type(elem)}")
            elif potential_type is None:
                potential_type = type(elem)

        for elem in elements:
            self.add(elem)
