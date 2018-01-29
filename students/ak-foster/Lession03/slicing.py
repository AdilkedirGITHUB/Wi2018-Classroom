# Return a copy of the sequence given after ordering transformation.

def split(s,x):
    """Given a sequence break into three variables defined globally."""
    ns = list(s)
    global first, last, middle
    first = ns[:x]
    last = ns[-x:]
    middle = ns[x:-x]


def build(s,ls):
    """Return a transformed copy with the same type as originally given sequence."""
    if type(s) == str:
        new_s = ''.join(ls)
        return new_s
    if type(s) == tuple:
        return tuple(ls)
    return ls


def first_last(s):
    """Return a copy of a given sequence with first and last items swapped."""
    split(s,1)
    global first, last, middle
    ls = last + middle + first
    return (build(s,ls))


def every_other(s):
    """Return a copy of a given sequence, but with every other item removed."""
    new_s = s[::2]
    return new_s


def fl4_every_other(s):
    """Return copy of a given sequence with first and last four items removed and remaining every other item removed"""
    return every_other(s[4:-4])


def reverse(s):
    new_s = s[::-1]
    return new_s


def sort_thirds(s):
    x = int(len(s)/3)
    split(s,x)
    global first, last, middle
    ls = middle + last + first
    return build(s,ls)


# Test block to verify the functions above work properly, throws error if not.
a_string = "this is a string"
a_tuple = (2, 54, 13, 77, 12, 5, 32, 1, 0, 33, 45, 19, 100)
a_list = ['thing', 'another', 'example','mixed', 'with', 'numbers', 0, 1, 2]
assert first_last(a_string) == "ghis is a strint"
assert first_last(a_tuple) == (100, 54, 13, 77, 12, 5, 32, 1, 0, 33, 45, 19, 2)
assert first_last(a_list) == [2, 'another', 'example','mixed', 'with', 'numbers', 0, 1,'thing']
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 12, 32, 0, 45, 100)
assert every_other(a_list) == ['thing', 'example', 'with', 0, 2]
assert fl4_every_other(a_string) == ' sas'
assert fl4_every_other(a_tuple) == (12, 32, 0)
assert fl4_every_other(a_list) == ['with']
assert reverse(a_string) == 'gnirts a si siht'
assert reverse(a_tuple) == (100, 19, 45, 33, 0, 1, 32, 5, 12, 77, 13, 54, 2)
assert reverse(a_list) == [2, 1, 0, 'numbers', 'with', 'mixed', 'example', 'another', 'thing']
assert sort_thirds(a_string) == 'is a stringthis '
assert sort_thirds(a_tuple) == (12, 5, 32, 1, 0, 33, 45, 19, 100, 2, 54, 13, 77)
assert sort_thirds(a_list) == ['mixed', 'with', 'numbers', 0, 1, 2, 'thing', 'another', 'example']
