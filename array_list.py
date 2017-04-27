# a List  is a List(array, int)
class List:
    def __init__(self, array, length):
        self.array = array
        self.length = length

    def __eq__(self, other):
        return ((type(other) == List)
          and self.array == other.array
          and self.length == other.length
        )

    def __repr__(self):
        return ("List({!r}, {!r})".format(self.array, self.length))


# none -> List
#returns an empty list
def empty_list():
    return List([], 0)

#List int val -> List
# adds a value to a list at the specified index
def add(al, idx, val):
    pass

#List -> int
#returns the number of elements in a list
def length(al):
    pass

#List int -> val
#returns the value in the list at the specified index
def get(al, idx):
    pass

#List int cal -> List
#returns a list