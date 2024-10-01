#!/usr/bin/python3


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.__head = None

    def __str__(self):
        """String representation of the entire list."""
        result = []
        current_node = self.__head
        while current_node:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new node into the list in sorted order."""
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
