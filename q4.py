import ctypes # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n=0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if k < 0 and abs(k) <= self._n: # within negative bounds
            # changes negative index to positive index equivalent b/c self._capacity variable causes
            # issues (i.e. the empty capacity space(s) at the end can be called with negative indices)
            return self._A[self._n + k]
        elif self._n < abs(k) or k == self._n: # out of bounds
            raise IndexError('invalid index')
        return self._A[k] # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c): # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A = B # use the bigger array
        self._capacity = c

    def _make_array(self, c): # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)( ) # see ctypes documentation
