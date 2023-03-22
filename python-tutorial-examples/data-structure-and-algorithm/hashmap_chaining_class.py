from node_class import Node
from singly_linked_lists_class import LinkedList


class HashMap:

    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    def hash(self, key):
        key_bites = key.encode()
        hash_code = sum(key_bites)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for item in list_at_array:
            if item[0] == key:
                item[1] == value

        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        for item in list_at_index:
            if item[0] == key:
                return item[1]

        return None
