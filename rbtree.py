__all__ = ['RBTree']

RB_RED = 0
RB_BLACK = 1


class RBIter(object):
  """An iterator for an RBTree"""

  def __init__(self, tree, start=None):
    """Stores the tree and possibly a pointer to an element"""
    self.tree = tree
    self.current = start if start is not None else 1 # TODO: Replace it with some reference to the internal structure of the tree.

  def move(self, count):
    """Moves the pointer with count steps(can be negative)"""
    pass

  def next(self):
    """This is the usual func of the iterator"""
    pass


class Node(object):
  """Node object to store the data in the tree"""
  __slots__ = ['key', 'data', 'color', 'left', 'right', 'parent', 'is_left', 'is_root']

  def __init__(self, key, data, color, left, right, parent, is_left, is_root=False):
    """We set the key, data, color and the children here"""
    self.key = key
    self.data = data
    self.color = color
    self.left = left
    self.right = right
    self.parent = parent
    self.is_left = is_left
    self.is_root = is_root
    pass


class Nil(object):
  pass


class RBTree(object):

  def __new__(cls, compare_func=None):
    """If compare_func is not None this function
       replaces the compare function with it"""
    pass

  def __compare(key1, key2):
    """Compares 2 keys"""
    pass

  def __init__(self):
    """Initialize the tree..."""
    self.nil = Nil()
    self.e_count = 0
    self.root = Node(None, None, None, None, None, None, None, True)
    pass

  def insert(self, key, data):
    """Insert data with a key"""
    pass

  def __setitem__(self, key, data):
    """Same as insert"""
    pass

  def remove(self, key):
    """Remove element with a given key"""
    pass

  def __delitem__(self, key):
    """Same as remove"""

  def search(self, key):
    """Search for a given key"""
    pass

  def __getitem__(self, key):
    """Same as search"""
    pass

  def max(self, key=False):
    """Returns the maximal element"""
    pass

  def min(self, key=False):
    """Returns the minimal element"""
    pass

  def __len__(self):
    """Returns the number of elements in the dict"""
    pass

  def get_ref(self, key):
    """Gets an ERef object on the element given by the key"""
    pass

  def __contains__(self, key):
    """Decides whether or not the key is in tree""" # in operator
    pass

  def __and__(self, other):
    """Takes the symmetric difference of trees"""
    pass

  def __or__(self, other):
    """Takes the union of trees"""
    pass

  def __xor__(self, other):
    """Takes the symmetric difference of trees"""
    pass

  def __iter__(self):
    """Returns an iterator to the tree"""
    pass

  def __left_rotate(self, curr):
    """Implements the left rotation step"""
    pass

  def __right_rotate(self, curr):
    """Implements the right rotation step"""
    pass

  def __restore_after_delete(self):
    """Restores the RB property after a delete"""
    pass

  def __restore_after_insert(self):
    """Restores the RB property after an insert"""
    pass

  def __real_find(self, key):
    """The real function used to find a key in the  tree"""
    pass

"""TODO:
- We could allow multiple iterators for a given tree.
- When iterators are created we should use a semaphore
  so that we can't modify(insert/delete) the tree while
  there are iterators on it.
"""