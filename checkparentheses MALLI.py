#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:Synopsis: Parentheses ordering checker.
:Author: <Your email>
:Date: <The date>
"""

from stack import Stack

def checkParentheses(sin):
  """Return whether the use of parentheses in the string `sin` is correct."""
  # Initialize the return value
  is_correct = None
  # Initialize a stack
  stack = Stack()
  # Use the stack to do the checking!
  raise NotImplementedError('Fix me!')
  # Return whether the use of parentheses in the string was correct
  return is_correct

# Example behaviour:
# Input string      Return value
# ()                True
# (()({}))          True
# aaa(vv)f[gg]df    True
# (                 False
# (]                False
# aa(b]b)ee         False

# EOF
