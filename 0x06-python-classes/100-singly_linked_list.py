#!/usr/bin/python3


"""Define classes for a singly-linked list."""


class Node:
    """Node class represents an element in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
        data (int): The data value of the node.
        next_node (Node): Reference to the next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of the node."""
        return self._data

    @data.setter
    def data(self, value):
        """Set the data value of the node."""
        if not isinstance(value, int):
            raise TypeError("Node data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Get or set the reference to the next node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("Next node must be a Node object or None")
        self._next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class represents a singly-linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self._head = None

    def sorted_insert(self, data):
        """
        Insert a new node into the list at the correct sorted position.

        Args:
        data (int): The data value for the new node.
        """
        new_node = Node(data)
        if self._head is None or self._head.data >= data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None:
                if current.next_node.data < data:
                    current = current.next_node
                else:
                    break
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        current = self._head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
