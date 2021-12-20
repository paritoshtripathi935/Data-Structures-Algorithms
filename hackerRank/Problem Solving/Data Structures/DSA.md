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

Certain functions associated with the vector are:
Iterators
begin() – Returns an iterator pointing to the first element in the vector
end() – Returns an iterator pointing to the theoretical element that follows the last element in the vector
rbegin() – Returns a reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
rend() – Returns a reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
cbegin() – Returns a constant iterator pointing to the first element in the vector.
cend() – Returns a constant iterator pointing to the theoretical element that follows the last element in the vector.
crbegin() – Returns a constant reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
crend() – Returns a constant reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
Capacity
size() – Returns the number of elements in the vector.
max_size() – Returns the maximum number of elements that the vector can hold.
capacity() – Returns the size of the storage space currently allocated to the vector expressed as number of elements.
resize(n) – Resizes the container so that it contains ‘n’ elements.
empty() – Returns whether the container is empty.
shrink_to_fit() – Reduces the capacity of the container to fit its size and destroys all elements beyond the capacity.
reserve() – Requests that the vector capacity be at least enough to contain n elements.
Element access:
reference operator [g] – Returns a reference to the element at position ‘g’ in the vector
at(g) – Returns a reference to the element at position ‘g’ in the vector
front() – Returns a reference to the first element in the vector
back() – Returns a reference to the last element in the vector
data() – Returns a direct pointer to the memory array used internally by the vector to store its owned elements.
Modifiers:
assign() – It assigns new value to the vector elements by replacing old ones
push_back() – It push the elements into a vector from the back
pop_back() – It is used to pop or remove elements from a vector from the back.
insert() – It inserts new elements before the element at the specified position
erase() – It is used to remove elements from a container from the specified position or range.
swap() – It is used to swap the contents of one vector with another vector of same type. Sizes may differ.
clear() – It is used to remove all the elements of the vector container
emplace() – It extends the container by inserting new element at position
emplace_back() – It is used to insert a new element into the vector container, the new element is added to the end of the vector
.
 

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



