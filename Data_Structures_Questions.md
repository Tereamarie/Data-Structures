Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?

ANSWER: 
    The time complexity for insertion is O(1) while deletion is O(n) (in the worst case) for a single operation. The amortized costs for both are O(1) since having to delete n elements from the queue still takes O(n) time.

2. What is the runtime complexity of `push` using a linked list?

ANSWER:
    The time complexity of Push or Pop Operation in the stack is O(1) i.e. Constant Time. # Because assignment operation takes constant time. The stack pointer or Top points to the topmost index of the stack. And assignment operation takes constant time.

3. What is the runtime complexity of `pop` using a list?

ANSWER:
     Removes the item at the given position in the list, and returns it. If no index is specified, pop() removes and returns the last item in the list.

4. What is the runtime complexity of `pop` using a linked list?

ANSWER:

5. What is the runtime complexity of `len` using a list?

ANSWER:
The len() function can be used on any sequence (such as a string, bytes, tuple, list, or range) or collection (such as a dictionary, set, or frozen set).

      a = ["bee", "moth", "ant"]
print(len(a))

6. What is the runtime complexity of `len` using a linked list?

ANSWER:
The append method is “amortized” O ( 1 ) O(1) O(1). In most cases, the memory required to append a new value has already been allocated, which is strictly O ( 1 ) O(1) O(1). Once the C array underlying the list has been exhausted, it must be expanded in order to accomodate further append s.

## Queue

1. What is the runtime complexity of `enqueue` using a list?

ANSWER:

Now remaining 1 operation can be 1 enqueue operation which will take O(1) time so total complexity in this case will be O(min(n,k)). Suppose we have k=1 and do (n-1) dequeue operations then it will take k*(n-1) time for multideqeue function and remaining one enqueue operation will take O(1) time 


2. What is the runtime complexity of `enqueue` using a linked list?

ANSWER:
enqueue and dequeue. Then implemented as a linked list, it can be done in O(1) complexity.



3. What is the runtime complexity of `dequeue` using a list?

ANSWER:
In a growing array, the amortized time complexity of all deque operations is O(1). Additionally, the time complexity of random access by index is O(1); but the time complexity of insertion or deletion in the middle is O(n)

4. What is the runtime complexity of `dequeue` using a linked list?

ANSWER:
In a doubly-linked list implementation and assuming no allocation/deallocation overhead, the time complexity of all deque operations is O(1). Additionally, the time complexity of insertion or deletion in the middle, given an iterator, is O(1); however, the time complexity of random access by index is O(n).


5. What is the runtime complexity of `len` using a list?

ANSWER:
len is an O(1) because in your RAM, lists are stored as tables (series of contiguous addresses). To know when the table stops the computer needs two things : length and start point. That is why len() is a O(1), the computer stores the value, so it just needs to look it up.


6. What is the runtime complexity of `len` using a linked list?

ANSWER:



## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

ANSWER:



2. What is the runtime complexity of `ListNode.insert_before`?

ANSWER:



3. What is the runtime complexity of `ListNode.delete`?

ANSWER:




4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

ANSWER:



5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

ANSWER:



6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

ANSWER:



7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

ANSWER:




8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

ANSWER:



9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

ANSWER:




10. What is the runtime complexity of `DoublyLinkedList.delete`?

ANSWER:



    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?


ANSWER:

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

ANSWER:


2. What is the runtime complexity of `contains`?
ANSWER:



3. What is the runtime complexity of `get_max`? 

ANSWER:



4. What is the runtime complexity of `for_each`?

ANSWER:


## Heap

1. What is the runtime complexity of `_bubble_up`?

ANSWER:



2. What is the runtime complexity of `_sift_down`?

ANSWER:



3. What is the runtime complexity of `insert`?

ANSWER:



4. What is the runtime complexity of `delete`?

ANSWER:


5. What is the runtime complexity of `get_max`?


ANSWER: