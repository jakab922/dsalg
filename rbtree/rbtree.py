__all__ = ['RBTree']


# Colors:

RED = 0
BLACK = 1

# EQ types

SMALLER = -1
EQUAL = 0
BIGGER = 1

# Child type

LEFT = 0
RIGHT = 1


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
  __slots__ = ['key', 'data', 'color', 'left', 'right', 'parent']

  def __init__(self, key, data, color, left, right, parent):
    """We set the key, data, color and the children here"""
    self.key = key
    self.data = data
    self.color = color
    self.left = left
    self.right = right
    self.parent = parent


class RBTree(object):

  def __new__(cls, compare_func=None, value_pref_func=None):
    """If compare_func is not None this function
       replaces the compare function with it"""
    pass

  def __compare(self, key1, key2):
    """Compares 2 keys"""
    if key1 < key2:
      return SMALLER
    elif key1 == key2:
      return EQUAL
    else:
      return BIGGER

  def __value_pref(self, key1, value1, key2, value2, op_type):
    """Used in conjunction with the &, | and ^ operators"""
    pass

  def __init__(self):
    """Initialize the tree..."""
    self.e_count = 0
    self.root = None
    self.first = None
    self.last = None

  def __find_item(self, key):
    """The real function used to find a key in the tree

    Returns a tuple where the first element indicates if
    the element in already in the tree and the second one
    is either a new element or the existing one from the tree.
    """
    curr = self.root
    par = None # Works well with empty tree as well
    while curr != None: # While we end up in a leaf
      comp = self.__compare(key, curr.key):
      if comp == SMALLER:
        par = curr
        curr = curr.left
      elif comp == EQUAL:
        return (True, curr)
      else:
        par = curr
        curr = curr.right

    return (None, par)

  def __find_first(self, cnode):
    cand = cnode
    while cnode:
      cand = cnode
      cnode = cnode.left
    return cand

  def __find_last(self, cnode):
    cand = cnode
    while cnode:
      cand = cnode
      cnode = cnode.right
    return cand

  def __set_relation(self, child, parent, rtype):
    if child:
      child.parent = parent
    if parent:
      if rtype == LEFT:
        parent.left = child
      else:
        parent.right = child

  def __left_rotate(self, cnode):
  """Implements the left rotation step"""
    assert cnode is not None and cnode.right is not None # TODO: Remove this line. It's only here for debugging purposes.
    onode = cnode.right

    self.__set_relation(onode.left, cnode, RIGHT)
    top_type = LEFT if cnode.parent and cnode.parent.left == cnode else RIGHT
    self.__set_relation(onode, cnode.parent, top_type)
    self.__set_relation(cnode, onode, LEFT)

  def __right_rotate(self, cnode):
  """Implements the right rotation step"""
    assert cnode is not None and cnode.left is not None # TODO: Remove this line. It's only here for debugging purposes.
    onode = cnode.left

    self.__set_relation(onode.right, cnode, LEFT)
    top_type = LEFT if cnode.parent and cnode.parent.left == cnode else RIGHT
    self.__set_relation(onode cnode.parent, top_type)
    self.__set_relation(cnode, onode, RIGHT)

  def __rotate(self, cnode, rtype):
    # TODO: Replace left+right rotation with this function since they are almost the same
    pass

  def __restore_after_delete(self, cnode):
    """Restores the RB property after a delete"""
    pass

  def __restore_after_insert(self, cnode):
    """Restores the RB property after an insert"""
    curr = cnode

    if curr.parent:
      if curr.parent == self.first and curr == curr.parent.left:
        self.first = curr
      if curr.parent == self.last and curr == curr.parent.right:
        self.last = curr

    while curr.parent and curr.parent.color == RED:
      par = curr.parent
      gpar = curr.parent.parent
      if par == gpar.left:
        unc = gpar.right
        if unc and unc.color == RED:
          par.color = BLACK
          unc.color = BLACK
          gpar.color = RED
          curr = gpar
        else:
          if curr == par.right:
            curr = par
            self.__left_rotate(curr)
          curr.parent.color = BLACK
          curr.parent.parent.color = RED
          self.__right_rotate(curr.parent.parent)
      else:
        unc = gpar.left:
        if unc and unc.color == RED:
          par.color = BLACK
          unc.color = BLACK
          gpar.color = RED
          curr = gpar
        else:
          if curr == par.left:
            curr = par
            self.__right_rotate(curr)
          curr.parent.color = BLACK
          curr.parent.parent = RED
          self.__left_rotate(curr.parent.parent)

    if not curr.parent: # It's a new root node
      curr.color = BLACK
      self.root = curr

  def insert(self, key, data):
    """Insert data with a key

    Returns True if the data was already in the tree,
    else it returns False.
    """
    node, parent = self.__find_item(key)
    if node is not None:
      is_in = True
    else:
      self.e_count += 1
      is_in = False
      node = Node(key, data, RED, None, None, parent)
      self.__restore_after_insert(node)
    node.data = data
    return is_in


  def __setitem__(self, key, data):
    """Same as insert"""
    pass

  def remove(self, key):
    """Remove element with a given key"""
    # TODO: Modify as we modified insert
    was_in, node = self.__find_item(key)
    if was_in:
      self.__restore_after_delete(node)
    return was_in

  def __delitem__(self, key):
    """Same as remove"""

  def search(self, key):
    """Search for a given key"""
    pass

  def __getitem__(self, key):
    """Same as search"""
    pass

  def __max(self, root_node=None):
    """Returns the maximal element in the subtree rooted at root_node or the real max if root_node is None"""
    if root_node is None:
      return self.last
    else:
      cand = root_node
      while cand is not None:
        cand = cand.right
      return cand

  def max(self):
    """Returns the maximal element"""
    return self.last

  def __min(self, root_node=None):
    """Returns the minimal element"""
    if root_node is None:
      return self.first
    else:
      cand = root_node
      while cand is not None:
        cand = cand.left
      return cand

  def __len__(self):
    """Returns the number of elements in the dict"""
    return self.e_count

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

  def __repr__(self):
    """Draws the tree in an idented way using dfs"""
    if self.root is not None:
      rpr = []
    else:
      return ''

    ident = '-'
    stack = [(self.root, 0, 0)]

    while stack:
      curr, lvl, ilvl = stack[-1]
      if curr is not None:
        if lvl == 0:
          rpr.append(ident * ilvl + curr.key)
        stack.append((curr.left if lvl == 0 else curr.right, 0, ilvl + 1))
      else:
        while stack and stack[-1][1] == 1:
          stack.pop()
        if stack:
          stack[-1] = (stack[-1][0], stack[-1][1] + 1, stack[-1][2])

    return ''.join(rpr)


"""TODO:
- We could allow multiple iterators for a given tree.
- When iterators are created we should use a semaphore
  so that we can't modify(insert/delete) the tree while
  there are iterators on it.
- Somehow we should make the balancing part and everything else
  as independent as possible.
- In a tree keys can be from different classes until a compare
  function is supported for __new__ which can handle this. Although
  any class that is a key(k) must not drop type error hash(k). Keys
  are stored as <class_name>.<hash> so if different types have the
  same hash we can still tell the difference. Node should have
  this hashed key and the real key. Maybe this part is an overshot.
  Can't really think of a usecase for this.
- Handle slice objects in __getitem__.
"""