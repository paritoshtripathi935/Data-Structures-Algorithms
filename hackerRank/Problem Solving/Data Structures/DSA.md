# Chapter 1 

## Complexity analysis

### Q1. Why is Complexity analysis needed?

Generally, there is always more than one way to solve a problem in computer science with different algorithms. Therefore, it is highly required to use a method to compare the solutions in order to judge which one is more optimal. The method must be:
Independent of the machine and its configuration, on which the algorithm is running on.
Shows a direct correlation with the number of inputs.
Can distinguish two algorithms clearly without ambiguity.

### Q2 What is time complexity?
Time Complexity: The time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input regardless of the machine. 
Consider two cases that created an algorithm to sort n numbers. 


We can see that initially, Shubham’s Algorithm was shining for smaller input but as the number of elements increases Rohan’s algorithm looks good.

### Q3. What are data structures ?
Ans.  A data structure is a way to store and organize data in a computer, so that it can be used efficiently.

We talk about data-structures as-
Mathematical/logical models or abstract data types  
Example of ADT - List
Store a given number of elements of any type.
Read elements by position 
Modify element at position 
Example of Concrete implementation - Arrays (linked list)

Abstract data types (ADT) - define data and operations but no implementation.

Some of the data structures we are going to learn are - Arrays, Linked List, Stack, queue, Tree, Graph.
We learn these things for above data structures - 
Logical views 
Operations
Cost of operations
Implementation

### Vector in c++ STL

Vectors are the same as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatically by the container. 
Vector elements are placed in contiguous storage so that they can be accessed and traversed using iterators. 
In vectors, data is inserted at the end. Inserting at the end takes differential time, as sometimes there may be a need to extend the array. 
Removing the last element takes only constant time because no resizing happens. Inserting and erasing at the beginning or in the middle is linear in time.
 

# List as abstract data type 

List (ADT) - 
Store a given number of elements of a given data-type
Write / modify elements at a position.
Read elements at a position.
Static list
Arrays (C.I) - 
Int A[10];
A[0] = 2;

# INTRODUCTION TO LINKED LIST

Int x;  // gives 4 bytes of memory
x= 8;

Int A[4]; // gives 16 bytes of memory
A[3] = 2; // constant time - array can access irrespective of size of array at constant time.

How to increase the size of an array?
Since the system assigned the memory for the array it cannot increase it size, to get size increased a new array is needed of large size and we have to copy elements of previous list.
It takes a lot of resources to get the new array with extended space, that's why they need a linked list data structure.

How to make a linked list and what is a linked list?

Linked List - A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:

6,5,4,2,3

Struct Node
{
Int data; // 4 bytes
Node * next; // 4 bytes
}

Access to elements: The time complexity of the linked list is 0(N).
Insertion: The time complexity of the linked list  is 0(N).



