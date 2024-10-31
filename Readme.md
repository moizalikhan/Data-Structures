### Git Commands

---

- ls, clear, mkdir"filename", cd, touch,
- rm"filename", rm -rf
- code"filename", mv-rename or move-, mv file1
- name, mv filename ./relativepath, mv filename ..
- cp Copy folderpath

# Python:

### Escape squence:

---

- \",\n \t "\\" "\\\\"
- concatenation, str(),\*
- input()-string, int, float
- variable order
- print( ,end = " ") -on the same line with space
- type() -for Data type

### String Methods:

---

- .split()-space, .split(",") comma
- string formatting- f{}, {}-.format()
- string index-[], negative index for last character and forward
- string slicing-[start: stop(at -1 and less than this no): step(less than this no) and also has -1 for reverse]
- len(), method-.lower(), .upper(), .title(), .count()
- For Removing Spaces- .strip(), .lstrip(), .rstrip(), .replace(" "--entity,""-replacing entity, count of the replacing entity)
- For finding position of a word or string- .find(string or character, starting position)
- For adding characters to string from left and right -center(len(string) + characters count, character)
- Strings are immutable- cannot change original string Operators in string- +, +=, \*=

### Control statements:

---

- if condition: or not condition -then check for empty or not
- else: -not possible with out if statement #also we can do nested if-else
- and operator, or operator
- elif condition:
- while condition: increment -while loop for which we don't know iterations and excute when the condition is true.
- for i in range(num+1): -if we have a definite count of iterations -for(10,0,-1)-for reversing numbers
- range(staring num, ending num+1, Step Argument) -range function, -for i in
  string_name or variable_name:
- Pass ,break-breaking the loop, continue -continuing the loop -keywords
- == -for euality
- True, False -Boolean in python
- Dry-Don't Repeat Yourself

### Functions:

---

- def name(parameters)- function definiion
- return- use more than print
- ="23" or None -as Default parameter
- Local and Global Scope -for understanding

### Lists:

---

- ["word1", "word2", "1"]-ordered collection of items
- [i]- for accessing members
- .append()- for adding data last to your list
- .insert(position,data)- for adding data to your desired position
- .extend(old_list or data)- for extending current list
- .pop()-Delete last element, .pop(position)-delete data on a position
- del list[i]- delete the member
- .remove('')-element that we do not know the position but want to delete it.
- if element in list -for checking element in the list
- .count(), .sort(), sorted()-just for print in order, .clear(), .copy()
- == -for Comparing
- is -for checking the list at the same location
- .split() -it converts string to list
- 'i'.join() -it converts list to string
- list are mutable
- for list[i] in list -looping through list
- matrix [i][inside index] -2d Matrix
- list(range(0,11)) -makes a list for us
- .index() -position of member
- you can pass a list as a argument
- .min() and .max()-min and max functions in python

### Tuples:

---

- ex = ('value1','value2') -- same as list but immutable, use for when data can't be changed, Tuples are faster
- .count(), .len(), .index(), slicing --[::]
- num('First_Element',)--->type(num)--> Type Tuple
- Tuple Unpacking, min(), max()
- Whenever Function can return 2 values then it is tuple
- Tuple can be converted to string and insert,append,pop,remove
- On tuple only count and index
- Tuple is Fast than List

### Dictionaries:

- unordered collections of data in key:value pair
- {'key': 'value'} or dict(key='value')
- Dictnories doesn't have index because of unordered pair
- for accessing data ---> dictname['key']
- Control statements with 'in' keyword
- .values() method, .keys=() method, .items() methods --> return tuples
- for i in dictonary_name:
  - print(Dictonary_name[i])
  - the above code prints the value of the keys
- tuple unpacking in dictonary
- .pop(), .popitem()---> removes any random key
- .update(passingDictname)
- .fromkeys("abc","unknown")---> Different keys
- .get("key", "default")--> if not present none
- d1 = d ---> much better to use .copy()

### Sets:

- s = {}
- Unordered collection of unique items
- you cannot store lists and Dictionaries in set
- .add(), .remove(), .discard(), .copy()
- No indexing
- union'|' and intersection '&'

### List Comprehension ---> Pythonic way:

- names_List = [i[0] for i in names]
- even_num = [i for i in range(1,11) if i%2 == 0]
- number_list_as_String = [str(i) for i in list1 if isinstance(i, (float, int))] ---> for if Statement
- even_or_odd_num = [i if i%2 == 0 else -i for i in range(1,11)] ---> for if and else Statement
- nested_list_comprehension = [[i for i in range(1,11)] for j in range(3)]

### Dictionary Comprehension---> Pythonic way:

- word_count = {char:string.count(char) for char in string}
- odd_even = {i:("even" if i%2 == 0 else 'odd') for i in range(1,11)}
- set_1 = {k\*\*2 for k in range(1,11)}

### Pass by value and Pass by reference:

- in pass by value it makes a copy and make changes to that not the original one.
- in pass by reference it takes the original value and makes changes to that with the help of &

### Time Complexity:

- The rate at which the time increases with the size of input. not execution time of system.
- Time Complexity compute at:
  - worst case
  - avoid constants
  - avoid lower values
- Big-O notation --> Upper bound --> worst case
- Theta notation --> Average complexity --> average case
- Omega notation --> Lower bound --> best case
- nested loops --> N\*\*2
- Space Complexity --> Auxilary space(space to solve the problem) and Input space(space to store the input) and also in bigO notation
- Advice: never do anything to the input

# Interview Notes:

DSA:

- Arrays:
  Math
  Loop
  Hashing-S
  sorts: Buddle, selection, insertion, Quick
  Linear, binary search
- Linkedlist:

* self is a reference to the current instance of a class. It allows you to access the instance’s attributes and methods from within the class.
* pointer is reference varable(head-->very first node and tail).

* Two pointers for reversal:
  def reversal(self):
  prev = None
  temp = self.head
  while(temp!=None):
  link = temp.next
  temp.next = prev
  prev = temp
  temp = link
  self.head = prev
  return self.head

* Remove duplicates: used sets.
  def removeduplicates(self):
  if(self.head == None):
  return
  temp = self.head
  setfor = set()
  setfor.add(temp.data)
  while(temp != None and temp.next!=None):
  if(temp.data == temp.next.data):
  temp.next = temp.next.next
  else:
  setfor.add(temp.next.data)
  temp = temp.next
  return setfor

* circular linkedlist:
  def insertatend(self, data):
  new_node = Node(data)
  if self.head is None:
  self.head = new_node
  self.tail = new_node
  new_node.next = self.head
  return
  self.tail.next = new_node
  self.tail = new_node
  self.tail.next = self.head

* Cycle detection: Fast and slow pointer
  def detect_cycle(self):
  slow_pointer = self.head
  fast_pointer = self.head.next

           while(fast_pointer!= None and fast_pointer.next!= None):
               slow_pointer = slow_pointer.next
               fast_pointer = fast_pointer.next.next

               if(slow_pointer == fast_pointer):
                   return True
           return False

  Binary trees:
  O(logn),
  effiecently searching data,
  unbalanced binary tree,
  for sorted data is not efficent.
  pointers can point to none.
  Complete binary tree, full binary tree(2or0).
  Binary search trees:
  levels = 0,1,2
  depth = from bottom up --> 0,1,2---> level wise --> 1,2,3

heap: (Olog n), max heap, min heap, insertion at the end and heapify to the above,ex: Priority Queues.

priority queue: higher priority are dequeued before elements with lower priority, implemented by: Heap, Unsorted list/array, Sorted list/array, CPU Scheduling.

Hashmaps: mapping keys to values using a hashing function(Hashing) and hashcode use as a index to store and retrieve data, ex: SHA-256, Hashing the Key,index=hash(key)%arraysize.

### Use Cases for **Arrays**:

1. **Random Access**: Arrays provide O(1) access time, making them ideal for situations where frequent random access to elements is required.

   - Example: **Storing indexed data**, like accessing specific elements in a lookup table.

2. **Static Data**: When the size of the data is known and fixed, arrays are efficient in terms of memory and performance.

   - Example: **Storing matrices or grids** (e.g., in image processing or mathematical computations).

3. **Contiguous Memory**: Arrays are stored in contiguous memory locations, making them cache-friendly and efficient for iteration.

   - Example: **Numeric computations** where large datasets are processed sequentially.

4. **Compact Storage**: Arrays are suitable for compact storage of large datasets with the same data type.

   - Example: **Storing large datasets** in scientific computing (e.g., Numpy arrays in Python).

5. **Multidimensional Data**: Arrays are well-suited for representing matrices, tables, and grids.
   - Example: **2D/3D data processing**, like image or game development.

### Use Cases for **Linked Lists**:

1. **Dynamic Data**: Linked lists allow efficient dynamic memory allocation, as they can grow and shrink without needing contiguous memory.

   - Example: **Dynamic data structures**, such as stacks, queues, and sparse matrices.

2. **Frequent Insertions/Deletions**: Linked lists are efficient for scenarios with frequent insertions or deletions, especially in the middle of the data.

   - Example: **Undo functionality** in applications or **managing playlists** where elements are frequently added or removed.

3. **Unknown Size or Growing Data**: When the size of the data is unknown or dynamically changes, linked lists are preferred because they can grow without resizing.

   - Example: **Implementing dynamic memory structures**, such as buffers that grow/shrink dynamically.

4. **Non-Contiguous Memory**: Linked lists do not require contiguous memory, making them efficient when memory fragmentation is an issue.

   - Example: **Managing memory in operating systems** or **storing large sets of sparse data**.

5. **Pointer-Based Structures**: Linked lists are ideal for implementing pointer-based structures like trees and graphs.
   - Example: **Binary search trees (BSTs)** or **adjacency lists** in graph algorithms.

### Summary:

- **Arrays** are ideal for random access, static data, and situations where data needs to be stored contiguously.
- **Linked lists** are better for dynamic memory allocation, frequent insertions and deletions, and non-contiguous memory storage.
