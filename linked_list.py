# an Anylist is one of,
# - None
# - Pair (value, Anylist)
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return ((type(other) == Pair)
          and self.first == other.first
          and self.rest == other.rest
        )

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest))

#None -> AnyList
# taking no arguments returns an empty list
def empty_list():
    return None

#AnyList int val-> Anylist
#adds a value to a list for the given integer given index or return IndexError if index is < 0 or > len(list)
def add(al, idx, val):
    if idx <= length(al) and idx >= 0:
        if al is None:
            if idx == 0:
                return Pair(val, None)
            else:
                return None
        else:
            if idx == 0:
                return Pair(al.first, Pair(val, al.rest))
            else:
                return Pair(al.first, add(al.rest, idx - 1, val))

#AnyList -> int
#returns the number of elements in a linked list
def length(al):
    if al == "mt":
        return 0
    else:
        return 1 + length(al.rest)
#AnyList int -> val
#returns the value of the list at the given index
def get(al, idx):
    if idx <= length(al) and idx >= 0:
        if al is None:
            if idx == 0:
                return None
        else:
            if idx == 0:
                return al.first
            else:
                return get(al.rest, idx -1)

# Anylist int val -> AnyList
#replaces the element at the specified index with the specified value
def set(al, idx, val):
    if idx <= length(al) and idx >= 0:
        if al is None:
            if idx == 0:
                return None
        else:
            if idx == 0:
                return Pair(val, al.rest)
            else:
                return Pair(al.first, set(al.rest, idx -1, val))

#AnyList int -> val AnyList
#returns a tuple of the value removed at the specified index and the remaining list
def remove(al, idx):
    if idx <= length(al) and idx >= 0:
        if al is None:
            return None
        else:
            if idx == 0:
                return al.rest
            else:
                return Pair(al.first, remove(al.rest, idx-1))



