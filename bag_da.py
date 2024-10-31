# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Bag ADT
# Description: Implements a Bag ADT using a Dynamic Array.

from dynamic_array import DynamicArray, DynamicArrayException

class Bag:
    def __init__(self, start_bag=None):
        """
        Initialize the Bag with an optional start array of values.
        Uses DynamicArray for internal storage.
        """
        self._data = DynamicArray()
        if start_bag:
            for value in start_bag:
                self.add(value)

    def __str__(self):
        """
        Returns a string representation of the Bag for debugging.
        """
        output = "BAG: {} elements. [".format(self._data.length())
        output += ', '.join([str(self._data.get_at_index(i)) for i in range(self._data.length())])
        return output + "]"

    def add(self, value: object) -> None:
        """
        Adds a new element to the Bag.
        O(1) amortized complexity.
        """
        self._data.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes one instance of the specified value from the Bag.
        Returns True if a value was removed; otherwise, False.
        """
        for i in range(self._data.length()):
            if self._data.get_at_index(i) == value:
                # Shift elements down to remove the value
                for j in range(i, self._data.length() - 1):
                    self._data.set_at_index(j, self._data.get_at_index(j + 1))
                self._data.remove_at_index(self._data.length() - 1)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Counts the occurrences of the specified value in the Bag.
        O(N) complexity.
        """
        count = 0
        for i in range(self._data.length()):
            if self._data.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears all elements from the Bag.
        O(1) complexity.
        """
        self._data = DynamicArray()

    def equal(self, second_bag: 'Bag') -> bool:
        """
        Compares the contents of this Bag with another Bag.
        Returns True if they contain the same elements with the same counts, otherwise False.
        O(N^2) complexity.
        """
        if self._data.length() != second_bag._data.length():
            return False

        checked_indices = set()
        for i in range(self._data.length()):
            found_match = False
            for j in range(second_bag._data.length()):
                if j in checked_indices:
                    continue
                if self._data.get_at_index(i) == second_bag._data.get_at_index(j):
                    checked_indices.add(j)
                    found_match = True
                    break
            if not found_match:
                return False
        return True

    def __iter__(self):
        """
        Initializes the iterator for the Bag.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Returns the next item in the Bag.
        """
        if self._index < self._data.length():
            value = self._data.get_at_index(self._index)
            self._index += 1
            return value
        else:
            raise StopIteration
