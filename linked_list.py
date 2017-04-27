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


# None -> AnyList
# taking no arguments returns an empty list
def empty_list():
    return None


# AnyList int val-> Anylist
# adds a value to a list for the given integer given index or return IndexError if index is < 0 or > len(list)
def add(al, idx, val):
    if al is None:
        if idx == 0:
            return Pair(val, None)
        else:
            raise IndexError()
    else:
        if idx == 0:
            return Pair(val, Pair(al.first, al.rest))
        else:
            return Pair(al.first, add(al.rest, idx - 1, val))


# AnyList -> int
# returns the number of elements in a linked list
def length(al):
    if al is None:
        return 0
    else:
        return 1 + length(al.rest)


# AnyList int -> val
# returns the value of the list at the given index
def get(al, idx):
    if al is None:
        raise IndexError()
    else:
        if idx == 0:
            return al.first
        else:
            return get(al.rest, idx - 1)


# Anylist int val -> AnyList
# replaces the element at the specified index with the specified value
def set(al, idx, val):
    if al is None:
       raise IndexError()
    else:
        if idx == 0:
            return Pair(val, al.rest)
        else:
            return Pair(al.first, set(al.rest, idx - 1, val))


# AnyList int -> val AnyList
# returns a tuple of the value removed at the specified index and the remaining list
def remove(al, idx, ret_val = "ret"):
    if al is None:
        raise IndexError()
    else:
        if idx == 0:
            if ret_val == "list":
                return al.rest
            elif ret_val == "removed":
                return al.first
            elif ret_val == "ret":
                return al.first, al.rest
        else:
            ret_list = Pair(al.first, remove(al.rest, idx -1, "list"))
            removed_val = remove(al.rest, idx -1, "removed")
            if ret_val == "ret":
                return removed_val, ret_list
            elif ret_val == "list":
                return ret_list
            elif ret_val == "removed":
                return removed_val



def main(al, idx):
    print(remove(al, idx))



