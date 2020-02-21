class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def isLLEmpty(self):
    return self.head == None

  def removefirstnode(self):
    if self.head is not None:
      self.head = self.head.next

  #method to prepend an item to the linked list
  def prepend(self,item):      
    new_node = Node(item)     #create a new node object with 'data' and 'next'
                              #upon instantiation, 'self.next' points to 'None'
                              #and 'self.data' is set equal to the input 'item' 
    new_node.next=self.head   #set new node 'next' field to the current head pointer
    self.head = new_node      #self.head now points to the new node

#linked list traversal to count number of nodes
  def nodecount(self):
    current = self.head
    count = 0
    while current is not None:
      count += 1
      current = current.next

    return count

#linked list traversal to search for an item
  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.data == item:
        found = True
      else:
        current = current.next

    return found

#linked list traversal to print node data
  def printItems(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

#linked list traversal to find the index of an item
  def IndexOf(self,item):
    current = self.head
    count = 0
    while current != None :
      if current.data == item:
        return count
      else:
        count+=1
        current = current.next

    return -1


llexamp=LinkedList()
print(llexamp.isLLEmpty())
#llexamp.prepend(21)
print(llexamp.isLLEmpty())
llexamp.prepend("Mercelis")
llexamp.prepend("Saquoya")
#llexamp.prepend(29)
#llexamp.prepend(100)
print(llexamp.nodecount())
llexamp.printItems()
#print(llexamp.search(32))
#print(llexamp.IndexOf(32))
llexamp.removefirstnode()
llexamp.printItems()
print(llexamp.nodecount())
llexamp.returnLast()


































"""Lab Exercises
1. 
   a. In the class Node, explain what 'init' is doing.
   b. Explain what 'init' is doing in the class LinkedList
   c. Explain how the 'prepend' method works in the LinkedList class
2. Draw a picture that explains how the 'removefirstnode' works.
3. Explain how the method 'isLLEmpty' works.
4. Modify the 'search' method so that it returns
    a. -1 if item not found
    b. the node index if item is found
  (i.e. so it works like 'IndexOf' for an array)
5. Implement the 'printItems' method
"""