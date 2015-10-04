#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:Synopsis: An implementation of a stack.
:Author: <Your email>
:Date: <The date>
"""

from linkedlist import LinkedList

class Stack:
  """
  A stack data structure object class.

  The implementation uses a `LinkedList` internally to store its data.

  Attributes:
    stack (LinkedList): The linked list that is used to store the
      objects added into the stack.
  """

  def __init__(self):
    """Initialize the stack."""
    self.stack = LinkedList()


  def push(self, obj):
    """Push a new object `obj` into the stack."""
    raise NotImplementedError('Fix me!')


  def pop(self):
    """Return and remove the (last added) object from the stack."""
    raise NotImplementedError('Fix me!')


  def top(self):
    """Return the (last added) object in the stack."""
    raise NotImplementedError('Fix me!')


  def isEmpty(self):
    """Return whether the stack is empty or not."""
    raise NotImplementedError('Fix me!')

# EOF
