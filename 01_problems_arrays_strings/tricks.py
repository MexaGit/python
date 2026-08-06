# Swapping the entry to be removed with the rightmost one in the array,
# and then deleting it
def delete(self, index):
    if self._size == 0:
        raise ValueError('Delete from an empty array')
    elif index < 0 or index >= self._size:
        raise ValueError(f'Index {index} out of range.')
    else:
        # Smart swapping” by overwriting the deleted element
        # (We don’t need to store the value that we are going to delete.)
        self._array[index] = self._array[self._size - 1]
        # The last element will be outside the populated chunk
        # (a word of caution: array loitering).
        self._size -= 1
