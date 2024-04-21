class OpenAddressingHashMap:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.count = 0
        self.threshold = 0.7

    def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self):
        new_size = self.size * 2
        new_keys = [None] * new_size
        new_values = [None] * new_size
        for i in range(self.size):
            if self.keys[i] is not None:
                index = self._hash(self.keys[i])
                while new_keys[index] is not None:
                    index = (index + 1) % new_size
                new_keys[index] = self.keys[i]
                new_values[index] = self.values[i]
        self.keys = new_keys
        self.values = new_values
        self.size = new_size

    def insert(self, key, value):
        if (self.count + 1) / self.size > self.threshold:
            self._rehash()

        index = self._hash(key)
        while self.keys[index] is not None:
            index = (index + 1) % self.size
            if index == self._hash(key):
                raise Exception('Hash table is full')
        self.keys[index] = key
        self.values[index] = value
        self.count += 1

    def search(self, key):
        index = self._hash(key)
        initial_index = index
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
            if index == initial_index:
                return None
        return None

    def delete(self, key):
        index = self._hash(key)
        initial_index = index
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.count -= 1
                return
            index = (index + 1) % self.size
            if index == initial_index:
                return
        return


# Create a hash map with size 10
hash_map = OpenAddressingHashMap(10)

# Insert some key-value pairs
hash_map.insert("apple", 5)
hash_map.insert("banana", 7)
hash_map.insert("orange", 3)

# Search for a key
print("Value for key 'banana':", hash_map.search("banana"))  # Output: Value for key 'banana': 7

# Update a value
hash_map.insert("banana", 10)
print("Updated value for key 'banana':", hash_map.search("banana"))  # Output: Updated value for key 'banana': 10

# Delete a key
hash_map.delete("orange")
print("Value for key 'orange' after deletion:", hash_map.search("orange"))  # Output: None
