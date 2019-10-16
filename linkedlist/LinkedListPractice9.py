##
# This problem is from chapter 2 lession 1
# The number of the problem is 9
#
# Please check Linked List Practice(NO:9) from Arrays and Linked Lists lession
#

import unittest

class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, value):

        if self.head is None:
            self.head = self.tail = Node(value)

        self.tail.next = Node(value)
        self.tail = self.tail.next

        return  self.tail.next


    def prepend(self, value):

        if self.head is None:
            self.head = self.tail = Node(value)
            return self.head
        node = Node(value)
        node.next = self.head
        self.head = node
        return self.head

    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        return None

    def to_list(self):
        values = []
        node = self.head
        while node:
            values.append(node.value)
            node = node.next

        return values

    def remove(self, value):
        """ Remove first occurrence of value. """

        # TODO: Write function to remove here

        pass

    def pop(self):
        """ Return the first node's value and remove it from the list. """

        # TODO: Write function to pop here

        pass

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """

        # TODO: Write function to insert here

        pass

    def size(self):
        """ Return the size or length of the linked list. """


        # TODO: Write function to get size here

        pass


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)

assert linked_list.to_list() == [1],[ "list contents: {linked_list.to_list()}"]
print (linked_list.to_list() == [1])
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], "list contents: {linked_list.to_list()}"
print (linked_list.to_list() == [2, 1, 3])
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
print