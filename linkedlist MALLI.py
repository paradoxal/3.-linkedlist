#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:File: linkedlist.py
:Author: <Your email>
:Date: <The date>
"""

class LinkedList:
  """
  A doubly linked list object class.

  The implementation makes use of a `ListNode` class that is used to
  store the references from each node to its predecessor and follower
  and to the data object associated with the node.

  Note: The position of a node can be defined with a value `n` which
  equals the number of nodes between it and the head of the linked list.
  In other words: The node that immediately follows the head guardian
  node is at position 0, its follower at position 1, and so on.
  """

  class ListNode:
    """
    A doubly linked list node object class.

    List nodes are ment to act as list element(/item) containers that
    wrap the objects inserted into the linked list.

    Attributes:
      obj (object): Any object that need to be stored
      follower (ListNode): The node that follows this (self) in the linked list
      predecessor (ListNode): The node that precedes this (self) in the linked list
    """

    def __init__(self, obj):
      """Initialize a list node object."""
      self.obj = obj
      self.follower = None
      self.predecessor = None


    def addAfter(self, node):
      """Adds node `node` as the follower."""
      tmp = self.follower
      self.follower = node
      node.predecessor = self
      node.follower = tmp
      if tmp:
        tmp.predecessor = node


    def removeAfter(self):
      """Removes the follower."""
      if self.follower:
        self.follower = self.follower.follower
        if self.follower:
          self.follower.predecessor = self


  def __init__(self):
    """Initialize the linked list."""
    # Does this seem reasonable?
    self.h = self.ListNode(None) # Left guardian (head)
    self.z = self.ListNode(None) # Right guardian (tail)
    self.h.addAfter(self.z)


  def _get_at(self, n):
    """Return the node at position `n`."""
    raise NotImplementedError('Fixme!')


  def addFirst(self, obj):
    """Add the object `obj` as the first element."""
    raise NotImplementedError('Fixme!')


  def addLast(self, obj):
    """Add the object `obj` as the last element."""
    raise NotImplementedError('Fixme!')


  def addPosition(self, n, obj):
    """Insert the object `obj` as the `n`th element."""
    raise NotImplementedError('Fixme!')


  def removePosition(self, n):
    """Remove the object at the `n`th position."""
    predecessor = self._get_at(n).predecessor
    if predecessor:
      predecessor.removeAfter()


  def getPosition(self, n):
    """Return the object at the `n`th position."""
    return self._get_at(n).obj


  def getSize(self):
    """Return the number of objects in the list."""
    raise NotImplementedError('Fixme!')

# EOF
