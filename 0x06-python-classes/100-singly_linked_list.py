#!/usr/bin/python3
""" This module defines a class Node which is a single linked list
and a SingleLinkedList which creates a sorted linked list"""


class Node:
    """ This class defines a single linked list
      where nodes are added to the list """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ This class creates a sorted linked list and inserts a new node into
    the list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None
                    and current.next_node.data < new_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data) + '\n'
            current = current.next_node
        return string.rstrip('\n')
