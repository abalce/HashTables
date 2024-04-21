class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        self.threshold = 0.7
        self.table = [[] for _ in range(size)]
        self.number_of_elements = 0
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.number_of_elements += 1
        if self.number_of_elements / self.size >= self.threshold:
            self._rehash()

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index]
                return
        raise KeyError("Key not found")

    def _rehash(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        for chain in self.table:
            for key, value in chain:
                index = hash(key) % new_size
                new_table[index].append([key,value])
        self.size = new_size
        self.table = new_table

hash_table = ChainedHashTable(10)
hash_table.insert(1, "apple")
hash_table.insert(2, "banana")
hash_table.insert(3, "cherry")

print(hash_table.search(2))
hash_table.delete(3)
print(hash_table.search(3))