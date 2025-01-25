#array
#records
#tuples

#queue
class circularQueue:
  def __init__ (self,length):
    self.length = length
    self.array = [None] * self.length
    self.front = -1
    self.rear = -1
    self.maxSize = len(self.array)

  def isEmpty(self):
    if self.array == [None] * self.length:
      return True
    else:
      return False
        
    
  def isFull(self):
    if (self.rear - 1 % self.front) == self.array[self.front]:
        return True
    else:
        return False

  def enqueue(self,newItem):
    if self.isFull():
      print("Queue full")
    else:
      self.rear = (self.rear + 1) % self.maxSize
      self.array[self.rear] = newItem

  def dequeue(self):
    if self.isEmpty():
      print("Queue empty")
    else:
      self.array[self.front + 1] = None
      self.front = (self.front + 1) % self.maxSize
      return self.array

  def show(self):
    print(self.array)
    return self.array, (self.front, self.rear)

#lists

#linked list
class Node:
  def __init__(self,data):
    self.data = data
    self.ref = None

class linkedList():
  def __init__(self):
    self.head = None

  def show(self):
    if self.head is None:
      print("Linked list is empty")
    else:
      n = self.head
      while n is not None:
        print(n.data," ")
        n = n.ref

  def prepend(self,data):
    new_node = Node(data) # New node is created
    new_node.ref = self.head # the Previous first element in linked list is now the second element
    self.head = new_node # self.head becomes the new element (the new node)

  def append(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      n = self.head
      while n.ref is not None:
        n = n.ref
      n.ref = new_node

  def insert(self,mode,data,x):
    if mode == "a":
      n = self.head
      while n is not None:
        if x==n.data:
          break
        n = n.ref
      if n is None:
        print("Item not in List")
      else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node

    elif mode == "b":
      if self.head is None:
        print("Linked list is empty")
        return
      if self.head.data == x:
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
      n = self.head
      while n is not None:
        if n.ref.data == x:
          break
        n = n.ref
      if n.ref == None:
        print("Node is not found")
      else:
        new_node = Node(data)
        new_node.ref = n.ref 
        n.ref = new_node

  def delete(self,mode,x=0 ):
    if mode == "b":
      if self.head == None:
        print("Linked list is empty, so we can't delete nay elements")
      else:
        self.head = self.head.ref
    elif mode == "e":
      if self.head == None:
        print("Linked list is empty, so we can't delete nay elements")
      elif self.head.ref == None:
        self.head = None
      else:
        n = self.head
        while n.ref.ref is not None:  # n.ref.ref means the reference of current node, then go to the Reference of THE NEXT NODE.. if n.ref starts at 3010 reference number, then n.ref.ref is the reference number after the node 3010.
          n = n.ref
        n.ref = None
    elif mode == "bv":
      if self.head is None:
        print("Can't delete linked list, because it is empty")
        return
      if x == self.head.data:
        self.head = self.head.ref
        return
      n = self.head
      while n.ref is not None:
        if x == n.ref.data:
          break
        n = n.ref
      if n.ref is None:
        print("Node isn't in the Linked list")
      else:
        n.ref = n.ref.ref



#stack               A STACK HAS NO FINITE SIZE
class Stack:
  def __init__(self,length):
    self.length = length
    self.array = [None] * self.length
    self.top = -1
    self.maxSize = len(self.array)
    self.__max = 4

  def isEmpty(self):
    if self.array == [None] * self.length:
      return True
    else:
      return False
    
  def isFull(self):
    if self.top == self.maxSize:
      return True
    else:
      return False
      
  def push(self,item):
    if self.isFull():
      print("Stack full")
    else:
      self.top = self.top + 1
      self.array[self.top] = item
      return self.array

  def pop(self):
    if self.isEmpty():
      print("Stack Empty")
    else:
      self.array[self.top] = None
      self.top = self.top - 1
      return self.array

  def peek(self):
    return self.array[self.top]

  def show(self):
    print(self.array)
    return self.array



#Hash Table

#Dictionary

#Graph

#Tree

def enqueue(array, element, priority):
  for i in range(len(array)):
    if priority < i[1]:
      array[i] = [item,priority]
  print(array)
a = []
while True:
  enqueue(a, "a",3)
    
  